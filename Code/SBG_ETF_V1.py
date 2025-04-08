# Copyright 2024 University of Texas at Austin, INGV Catania
# Author: Dr. James Thompson, Dr. Claudia Corradino

from SBG_ETF_Functions import *
import numpy as np
import random
import itertools
import pandas as pd
from osgeo import gdal
import time
import tqdm
import matplotlib.pyplot as plt 
import json

#rad_file = './SBG_OTTER_L1_1862700_01_20180130_1939_1948_V01.hdr' #Input radiance file (ENVI format)
#rad_file = './SBG_OTTER_L1_1862700_01_20180130_1939_1948_V01_rad.tif' #Input radiance file (geotiff format) VOLCANO
#rad_file = './SBG_OTTER_v003_L1_1662900_10_20160617_2045_2103_V01.tif' #Input radiance file (geotiff format) FIRE
rad_file = './Bardarbunga_20140923_123000_VNPP_georef_60m_SBG_SW_TIF.tif' #Input radiance file (geotiff format) Bardarbunga file
meta_file = './OTTER_META_ETF_EX.json'

#load metafile
with open(meta_file) as json_file:
    metadata = json.load(json_file)

if ".tif" not in rad_file:
    rad_file_wl = read_envi_wavelengths(rad_file)
else:
    rad_file_wl = [3.98, 4.8, 8.32, 8.63, 9.07, 10.3, 11.35, 12.05]

radiance_dataset = gdal.Open(rad_file, gdal.GA_ReadOnly)
img_dat_input = radiance_dataset.ReadAsArray()

if ".tif" not in rad_file:
    img_dat_input = np.transpose(img_dat_input, (2, 1, 0)) # Flip the dimensions to (594, 2583, 6)
else:
    img_dat_input = np.transpose(img_dat_input, (1, 2, 0)) # Flip the dimensions to (594, 2583, 6)

x_len = radiance_dataset.RasterXSize
y_len = radiance_dataset.RasterYSize

#change as needed
daynight = 'day'

MIRBand = 0
k = 0
c1 = 119104200
c2 = 14387.75
wavelen = [3.98, 4.8, 8.32, 8.63, 9.07, 10.3, 11.35, 12.05]

iSceneRad_1=img_dat_input[:,:,0]
iSceneRad_7=img_dat_input[:,:,6]
iSceneRad_8=img_dat_input[:,:,7]
iSceneRad_1=np.where(iSceneRad_1 <= 0, np.nan, iSceneRad_1)
iSceneRad_7=np.where(iSceneRad_7 <= 0, np.nan, iSceneRad_7)
iSceneRad_8=np.where(iSceneRad_8 <= 0, np.nan, iSceneRad_8)

iSceneTemp_7 = c2 / (wavelen[6] * np.log(c1 / ((wavelen[6]**5) * iSceneRad_7 + 1)))
iSceneTemp_8 = c2 / (wavelen[7] * np.log(c1 / ((wavelen[7]**5) * iSceneRad_8 + 1)))
ROInan = np.ones(np.shape(iSceneRad_8))

dNTI, S2, NTI1, NTInan = CalcNTI(iSceneRad_1, iSceneRad_8, ROInan, daynight)
dETI, S4 = CalcETI(iSceneTemp_8, iSceneRad_8, ROInan, NTI1, NTInan, daynight, wavelen, MIRBand, c1, c2)
NTIThreshold = -0.8 if daynight == 'night' else -0.6

alert2 = (dNTI > S2) & (dETI > S4)
alert3 = NTInan >= NTIThreshold

ROInan = ~alert2 & ~alert3

dNTI, S2, NTI1, NTInan = CalcNTI(iSceneRad_1, iSceneRad_8, ROInan, daynight)
dETI, S4 = CalcETI(iSceneTemp_8, iSceneRad_8, ROInan, NTI1, NTInan, daynight, wavelen, MIRBand, c1, c2) #inserire try excempt

alert2b = (dNTI > S2) & (dETI > S4)

ROInan2 = ~alert2 & ~alert3 & ~alert2b
alert = ~ROInan2
#alertnan = np.where(alert == 0, np.nan, alert)
BT7masked = iSceneTemp_7.copy()
BT7masked=np.where(alert == 0, 0, BT7masked)
anomaly_uncertainty = BT7masked.copy()*0.005
n_anom = np.sum(alert)

NoData = round(-9999)
BT7masked=np.where(alert == 0, NoData, BT7masked)
anomaly_uncertainty=np.where(alert == 0, NoData, anomaly_uncertainty)
data_quality = np.zeros_like(anomaly_uncertainty, dtype='int8')
overall_quality = int(np.median(data_quality))

#%%
output_name = rad_file[0:rad_file.rfind("_")]+'_ETF.tif'

#get file driver
#output_Driver = radiance_dataset.GetDriver()
output_Driver = gdal.GetDriverByName('GTiff')

#Create new raster
file_output_ETF = output_Driver.Create(output_name, \
                    xsize=radiance_dataset.RasterXSize, ysize=radiance_dataset.RasterYSize, \
                    bands=3, eType=gdal.GDT_Float32)#, options={"BAND_NAMES": "1,2,3"})#bands=len(library_classes)

# Set metadata
file_output_ETF.SetGeoTransform(radiance_dataset.GetGeoTransform())
file_output_ETF.SetProjection(radiance_dataset.GetProjection())
file_output_ETF.GetRasterBand(1).WriteArray(BT7masked)
file_output_ETF.GetRasterBand(1).SetCategoryNames(['Surface Temperature'])
file_output_ETF.GetRasterBand(1).SetMetadataItem('band names', 'Surface Temperature','ENVI')
file_output_ETF.GetRasterBand(1).SetDescription('Surface Temperature')
file_output_ETF.GetRasterBand(1).SetUnitType('Kelvin')
file_output_ETF.GetRasterBand(1).SetNoDataValue(NoData)
file_output_ETF.GetRasterBand(2).WriteArray(anomaly_uncertainty)
file_output_ETF.GetRasterBand(2).SetCategoryNames(['Temperature Uncertainty'])
file_output_ETF.GetRasterBand(2).SetMetadataItem('band names', 'Temperature Uncertainty','ENVI')
file_output_ETF.GetRasterBand(2).SetDescription('Temperature Uncertainty')
file_output_ETF.GetRasterBand(2).SetUnitType('Kelvin')
file_output_ETF.GetRasterBand(2).SetNoDataValue(NoData)
file_output_ETF.GetRasterBand(3).WriteArray(data_quality)
file_output_ETF.GetRasterBand(3).SetCategoryNames(['Data Quality'])
file_output_ETF.GetRasterBand(3).SetMetadataItem('band names', 'Data Quality','ENVI')
file_output_ETF.GetRasterBand(3).SetDescription('Data Quality')
file_output_ETF.GetRasterBand(3).SetUnitType('None')
file_output_ETF.GetRasterBand(3).SetScale(0)
file_output_ETF.GetRasterBand(3).SetNoDataValue(NoData)
file_output_ETF.SetMetadata({'Number of Anomalies': str(n_anom), 'anomaly_threshold': str([S2,S4]), 'overall_quality': str(overall_quality)})
#file_output_ETF.SetMetadata({'band names': ['Surface Temperature','Temperature Uncertainty','Data Quality']})
file_output_ETF.SetMetadataItem('band names', 'Surface Temperature,Surface Temperature','ENVI')
                                                
#close data file
file_output_ETF = None

#determine metadata file
metadata["ProductMetadata"]["BandSpecification"] = ['Surface Temperature','Temperature Uncertainty','Data Quality']
metadata["ProductMetadata"]["NumberOfBands"] = 3
metadata["ProductMetadata"]["UnitType"] = "Kelvin"
metadata["ProductMetadata"]["NoData"] = NoData

#save metadata file
json_object = json.dumps(metadata, indent = 4) 
with open(output_name[:-4]+'.json', 'w') as outfile: 
    outfile.write(json_object)
