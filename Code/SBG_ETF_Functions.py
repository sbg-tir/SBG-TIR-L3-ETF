# Copyright 2024 University of Texas at Austin, INGV Catania
# Author: Dr. James Thompson, Claudia Corradino

import numpy as np
import random
import itertools
import pandas as pd
import time
import tqdm

def planck_radiance(T, wavelength, c1, c2):
    """
    Calculate the spectral radiance using the Planck function.
    :param T: Temperature in Kelvin
    :param wavelength: Wavelength in micrometers (um)
    :param c1: First radiation constant
    :param c2: Second radiation constant
    :return: Spectral radiance in W/(m^2·sr·um)
    """
    exponent = c2 / (wavelength * T)
    # Prevent overflow by capping the exponent
    #exponent = np.clip(exponent, 0, 700)
    radiance = (c1 * wavelength**-5) / (np.exp(exponent) - 1)
    
    return radiance



def radiance_verification():
    """
    Verifies the radiance calculations for multiple bands based on temperature and wavelength.
    """
    # Dictionary of wavelengths for ECOSTRESS bands 2 to 6
    wavelengths = {
        2: 8.29,  # Example wavelength for band 2 
        3: 8.78,  # Example wavelength for band 3
        4: 9.2,   # Example wavelength for band 4
        5: 10.49,  # Example wavelength for band 5
        6: 12.09   # Example wavelength for band 6

    }

    # Planck constants 
    c1 = 1.191042e8 # for wavelength given in micrometers
    c2 = 1.4387752e4 # for wavelength given in micrometers
    
    t325 = 325  # Temperature in Kelvin
    t295 = 295  # Temperature in Kelvin

    # Iterate through bands 2 to 6 for radiance calculation
    for band in range(2, 7):
        # Get the center wavelength for the current band
        wavelength = wavelengths.get(band)

        # Calculate radiance for the two temperatures
        radiance_325 = planck_radiance(t325, wavelength, c1, c2)
        radiance_295 = planck_radiance(t295, wavelength, c1, c2)

        # Print the results for each band
        print(f"Calculated radiance at 325K for wavelength {wavelength}: {radiance_325}")
        print(f"Calculated radiance at 295K for wavelength {wavelength}: {radiance_295}")



def read_envi_wavelengths(filename, nm=True):
    header_name = filename.split(".")[0] + ".hdr"
    with open(header_name, "r") as header_file:
        header = header_file.readlines()

    for line in header:
        if "wavelength = {" in line or "wavelength= {" in line or "wavelength={" in line:
            header = line
            break

    wavelengths = [float(x.strip()) for x in header.split("{")[1].split("}")[0].split(",")]
    return wavelengths

def CalcNTI(iSceneRad_1, iSceneRad_8, ROInan, daynight):
    NTI = (iSceneRad_1 - iSceneRad_8) / (iSceneRad_1 + iSceneRad_8)
    NTInan = NTI * ROInan

    Threshold = -0.8 if daynight == 'night' else -0.6

    alert3 = NTInan >= Threshold

    NTI1 = NTInan * ~alert3
    NTI1[NTI1 == 0] = np.nan
    NTI1_pad=np.pad(NTI1,pad_width=1)
    NTIbk = np.nanmean(np.lib.stride_tricks.sliding_window_view(NTI1_pad, (3, 3)), axis=(2, 3)) #!!
    dNTI = NTI1 - NTIbk
    dNTI[dNTI < -0.1] = np.nan

    dNTImu = np.nanmean(dNTI)
    dNTIsig = np.nanstd(dNTI)

    S2 = min([(dNTImu + (5 * dNTIsig)), 0.03]) if daynight == 'night' else min([(dNTImu + (15 * dNTIsig)), 0.035])

    return dNTI, S2, NTI1, NTInan

def CalcETI(iSceneTemp_8, iSceneRad_8, ROInan, NTI1, NTInan,
             daynight, wavelen, MIRBand, c1, c2):

    # Step 2: Calculate the apparent MIR radiance with the brightness temperature that TIR picks up
    Rad_app_MIR = c1 / ((wavelen[MIRBand] ** 5) * (np.exp(c2 / (wavelen[MIRBand] * iSceneTemp_8)) - 1))
    NTIapp = (Rad_app_MIR - iSceneRad_8) / (Rad_app_MIR + iSceneRad_8)
    NTIappnan = NTIapp * ROInan

    all_NTIappnan = NTIappnan.flatten()
    all_NTI1 = NTInan.flatten()
    nonnanNTI1 = ~np.isnan(all_NTI1)&~np.isnan(all_NTIappnan)
    try:
      NTIapp_p = np.polyfit(all_NTIappnan[nonnanNTI1], all_NTI1[nonnanNTI1], 2)#!
      NTIref = np.polyval(NTIapp_p, NTIapp)
      ETI = NTI1 - NTIref
      ETI_pad=np.pad(ETI,pad_width=1)
      ETIbk = np.nanmean(np.lib.stride_tricks.sliding_window_view(ETI_pad, (3, 3)), axis=(2, 3)) #!!
      dETI = ETI - ETIbk

      dETImu = np.nanmean(dETI)
      dETIsig = np.nanstd(dETI)

      if daynight == 'night':
        S4 = min(dETImu + (5 * dETIsig), 0.02)
      else:
        S4 = min(dETImu + (15 * dETIsig), 0.035)
    except:
      print("Fitting does not apply")    
      dETI=np.zeros(NTI1.shape)
      S4=np.zeros(NTI1.shape)
    return dETI, S4
