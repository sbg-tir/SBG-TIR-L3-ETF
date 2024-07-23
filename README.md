# Surface Biology and Geology (SBG) Observing Terrestrial Thermal Emission Radiometer (OTTER)

## SBG-TIR OTTER Level 3 Elevated Temperature Features (L3-ETF) Data Product Algorithm

[Michael S. Ramsey](https://github.com/michaelsramsey)<br>
[mramsey@pitt.edu](mailto:mramsey@pitt.edu)<br>
University of Pittsburgh

[James O. Thompson](https://github.com/jthompson2710)<br>
[james.thompson@beg.utexas.edu](mailto:james.thompson@beg.utexas.edu)<br>
University of Texas Austin

[Claudia Corradino](https://github.com/clacor89)<br> 
[claudia.corradino@ingv.it](claudia.corradino@ingv.it)<br>
National Institute of Geophysics and Volcanology (INGV) – Etna Volcano Observatory


# Abstract
The 2017-2027 Decadal Survey for Earth Science and Applications from Space (ESAS 2017) was released in January 2018. ESAS 2017 was driven by input from the scientific community and policy experts and provides a strategic vision for the next decade of Earth observation that informs federal agencies responsible for the planning and execution of civilian space-based Earth-system programs in the coming decade. These include the National Aeronautics and Space Administration (NASA), the National Oceanic and Atmospheric Administration (NOAA), and the U.S. Geological Survey (USGS). NASA has, thus far, utilized this document as a guide to inform exploration of new Earth mission concepts that are later considered as can-didates for fully funded missions. High-priority emphasis areas and targeted observables include global-scale Earth science questions related to hydrology, ecosystems, weather, climate, and solid earth. One of the Designated Observables (DO’s) identified by ESAS 2017 was Surface Biology and Geology (SBG) with a goal to acquire concurrent global hyperspectral visible to shortwave infrared (VSWIR; 380–2500 nm) and multispectral midwave and thermal infrared (MWIR: 3–5 μm; TIR: 8–12 μm) image data at high spatial resolution (~30 m in the VSWIR and ~ 60 m in the TIR) at sub-monthly temporal resolution globally. The final sensor characteristics will be determined during the mission formulation phase, but ESAS 2017 provides guidance for a VSWIR instrument with 30–45 m pixel resolution, ≤16 day global revisit, SNR > 400 in the VNIR, SNR > 250 in the SWIR, and 10 nm sampling in the range 380–2500 nm. It also recommends a TIR instrument with more than five channels in 8–12 μm, and at least one channel at 4 μm, ≤60 m pixel resolution, ≤3 day global revisit, and noise equivalent delta temperature (NEdT) ≤0.2 K (NASEM, 2018; Schimel et al., 2020). Alone, SBG will provide a comprehensive global monitoring for multiple scientific disciplines. Complemented with systems like Landsat and Sentinel-2 VSWIR, global change processes with faster than 16-day global change rates can be mapped. Further, complimented with planned TIR systems such as LSTM and TRISHNA, the temporal revisit could be as frequent as 1-day at the equator, making the system excellent for tracking dynamic thermal features and hazards. This document will grow to fully describe the planned Elevated Temperature Features (ETF) product for the SBG TIR data.

_______________________________________________________________________________________________________________________
<i>This repository will gradually expand to contain the Surface Biology and Geology Thermal Infrared (SBG-TIR) OTTER level 3 elevated temperature features (L3-ETF) data product algorithm. </i>
_______________________________________________________________________________________________________________________


## Level 3 Algorithm Theoretical Basis Document (ATBD): [click here](/SBG_L3_ATBD_ETF_20231107.pdf)
## Level 3 Product Specification Document (PSD): [click here](/SBG-TIR_PSD_L3_ETF_20231107.pdf)

#  [INTRODUCTION]{.smallcaps}

## Identification

This is the Product Specification Document (PSD) for Level 3 (L3) Elevated Temperautre Features (ETF) data product of NASA's Surface Biology and Geology -- Thermal Infrared (SBG-TIR) mission. The SBG-TIR L3 ETF product provides elevated temperature features generated from data acquired by the SBG-TIR radiometer instrument according to the ETF algorithm described in the SBG-TIR L3 ETF Algorithm Theoretical Basis Document (ATBD) (D-1000786).

## Purpose and Scope

The "Preliminary Product Specification Document" (PPSD) is an initial "Phase A" version of the Product Specification Document (PSD), describing the Standard and Low Latency Level 3 ETF product generated using the ETF algorithm. These include the detailed descriptions of the format and contents of the product and ancillary files that will be delivered to the Land Process Distributed Active Archive Center (LP-DAAC).

## Mission Overview

NASA's SBG mission was a Designated Observable (DO) identified in the National Academies of Sciences, Engineering and Medicine (NASEM) 2017 Decadal Survey. The Decadal Survey document presented a clear vision for the combined roles of visible to shortwave infrared imaging spectroscopy and multispectral or hyperspectral thermal infrared image data in addressing terrestrial and aquatic ecosystems and other elements of biodiversity, geology, natural hazards, the water cycle, and applied sciences topics relevant to many areas with societal benefits. 

The SBG-TIR portion of the mission develops the TIR multispectral instrument. The SBG-TIR instrument measures the emitted radiance of the Earth surface and uses that information to better understand the dynamics of Earth's changing surface geology and biology, ground/water temperature, snow reflectivity, active geologic processes, vegetation traits, and algal biomass. The SGB-TIR mission is also a cooperative effort with the Italian Space Agency (Agenzia Spaziale Italiana; ASI), which provides SBG-TIR platform metadata and Visual and Near-Infrared (VNIR) products. Descriptions of partner products are covered in separate documents.

SBG-TIR mission addresses the following most important and very important priorities as highlighted by the Decadal Survey:

Most Important

Ecosystems

E1a: Quantify the distribution of the functional traits, functional types, and composition of vegetation and marine biomass, spatially and over time.

E1c: Quantify the physiological dynamics of terrestrial and aquatic primary producers.

E2a: Quantify the fluxes of CO~2~ and CH~4~ globally at spatial scales of 100 to 500 km and monthly temporal resolution with uncertainty \<25% between land ecosystems and atmosphere and between ocean ecosystems and atmosphere.

Hydrology

H1c: Quantify rates of snow accumulation, snowmelt, ice melt, and sublimation from snow and ice worldwide at scales driven by topographic variability.

Solid Earth

S1a: Measure the pre-, syn-, and posteruption surface deformation and products of Earth's entire active land volcano inventory at a time scale of days to weeks.

Very Important

Ecosystems

E1a: Quantify the distribution of the functional traits, functional types, and composition of vegetation and marine biomass, spatially and over time.

Hydrology

H2a: Quantify how changes in land use, water use, and water storage affect evapotranspiration rates, and how these in turn affect local and regional precipitation systems, groundwater recharge, temperature extremes, and carbon cycling.

H4a: Monitor and understand hazard response in rugged terrain and land margins to heavy rainfall, temperature and evaporation extremes, and strong winds at multiple temporal and spatial scales. This socioeconomic priority depends on success of addressing H1b and H1c, H2a, and H2c.

Solid Earth

S1c: Forecast and monitor landslides, especially those near population centers.

S2b: Assess surface deformation (\<10 mm), extent of surface change (\<100 m spatial resolution) and atmospheric contamination, and the composition and temperature of volcanic products following a volcanic eruption (hourly to daily temporal sampling).

Climate

C3a: Quantify CO~2~ fluxes at spatial scales of 100-500 km and monthly temporal resolution with uncertainty \<25% to enable regional-scale process attribution explaining year-to-year variability by net uptake of carbon by terrestrial ecosystems (i.e., determine how much carbon uptake results from processes such as CO~2~ and nitrogen fertilization, forest regrowth, and changing ecosystem demography.)

Weather

W3a: Determine how spatial variability in surface characteristics modifies regional cycles of energy, water and momentum (stress) to an accuracy of 10 W/m^2^ in the enthalpy flux, and 0.1 N/m^2^ in stress, and observe total precipitation to an average accuracy of 15% over oceans and/or 25% over land and ice surfaces averaged over a 100 × 100 km region and 2- to 3-day time period.

The SBG-TIR mission answers these questions by accurately measuring the emitted radiance of Earth's surface in the mid-infrared (MIR) and TIR spectral regions using a multispectral radiometer. The instrument measures radiance data in 8 spectral bands from 3.95 to 12.05 m with approximately 60 meter spatial resolution at nadir and a nominal revisit time of 3 days at the equator.

## Applicable and Reference Documents

"Applicable" documents levy requirements on the areas addressed in this document. "Reference" documents are identified in the text of this document only to provide additional information to readers. Unless stated otherwise, the document revision level is Initial Release. Document dates are not listed, as they are redundant with the revision level.

1.  **Applicable Documents**

<!-- -->

1.  SBG-TIR Project Science Data System Requirements (TBD)

2.  SBG-TIR Science Data Management Plan (TBD)

3.  ICD Between SBG-TIR SDS and LPDAAC (TBD)

4.  SBG-TIR Level 1 Geolocation Algorithm Theoretical Basis Document (TBD)

5.  SBG-TIR Level 1 Calibration Algorithm Theoretical Basis Document (TBD)

6.  SBG-TIR Level 1 Product Specification Document (TBD)

7.  SBG-TIR Level 2 Algorithm Theoretical Basis Documents (TBD)

8.  SBG-TIR Level 2 Product Specification Document (TBD)

9.  SBG-TIR Project Level 3 Science Data System Requirements (TBD)

10. SBG-TIR Level 3 ETF Algorithm Theoretical Basis Document (TBD)

    1.  **Reference Documents**

2017-2027 Decadal Survey for Earth Science and Applications from Space (ESAS 2017)

SBG Science and Applications Tracibility Matirx (SATM)

## SBG-TIR Data Products

SBG-TIR Level 0 data primarily consist of spacecraft packets that have been pre-processed by the Ground Data System (GDS). Level 1 provides foundational calibration and geolocation products, including spacecraft engineering data, time-tagged raw sensor pixels (appended with their radiometric calibration coefficients), black body pixels (used to generate the calibration coefficients), geolocated and radiometrically calibrated at-sensor radiances (for each image pixel), and corrected spacecraft attitude data. Level 2 provides scientific-ready products such as the land surface temperature (LST) and emissivities of each spectral band retrieved from the at-sensor radiance data, and a cloud mask. Level 3 and L4 are more advanced scientific products derived from Level 2 data and external ancillary data. A summary Product Grouping list is shown in Table 1-1. This document will only describe the L3 ETF product.

| **Areas** | **Product** | **ShortName** | 
| --- | --- | --- |
| Fundamental (Level 1) | Radiance at Sensor | RAS |
| Fundamental | Surface Temperature and Emissivity | LSTE (incl WT, ST, and SGC) |
| Fundamental | Cloud mask | CM |
| Plant Functional Traits Suite | Evapotranspiration<br> Water Use Efficiency<br> Evaporative Stress Index | ET<br> WUE<br> ESI |
| Geology Suite | Surface Minerology (TIR only)<br> Elevated Technical Features<br> Volcanic Activity | SM<br> ETF<br> VA |
| Snow Physics Suite | Snow Temperature (Use fundamental LST&E) | --- |
| Aquatics Biology/Biogeochemistry Suite | Water Temperature (Use fundamental LST&E) | --- |

*Table 1-1: SBG-TIR Product Groups*

2.  **Level 3 ETF Product Overview**

SBG-TIR provides a Level 3 product to identify elevated temperature features. This product will contain layers for surface temperature, temperature uncertainty, and data quality for pixels that are flagged as exhibiting elevated temperature features. This product is intended to be used in the detection and monitoring of wildfire and lava flows.

The L3 gridded products are resampled to a map grid with a fixed 60m pixel size, and are used to create 110x110km tile images following the "Sentinel-2 Tiling Grid". Tiled products are provided in Cloud Optimized GeoTIFF (COG) format (UTM/WGS84). See Section 3 for detailed descriptions of the product.

3.  **Level 3 ETF Standard Day, Night, and Low Latency Products**

The L3 ETF detection algorithm will be run during the day and night over land. The "Standard" products are expected to be processed and delivered within 72 hours of their collection. However, a special subset of L3 products will be generated within 24 hours of collection to meet special time-critical science requirements. These "Low Latency" products will be processed using the Low Latency geolocation radiance input only, which may be improved in the standard product. Therefore, the L3 Low Latency product will differ slightly from the subsequent Standard product, and may not be archived after serving their short-term purposes.

4.  **Level 3 ETF Intermediate and Distributable Products**

The L3 EFT product computes an intermediate background temperature value for thresholding. This value is provided in product metadata accompanying the L3 ETF product.

5.  **Level 3 ETF PGE Overview**

L3 products are produced by a Product Generation Executable (PGE) that ingests the L1B Radiance and Geolocation data. *(More info to be added in summary once algorithm is finalized)*

## 2. Data Product Organization
### 2.1. Product File Format

SBG-TIR image products are distributed in either (or both) of two formats: "Network Common Data Form 4" (netCDF-4), or "Cloud-Optimized GeoTIFF" (COG). Only the L1A, L1B and L2 swath products are provided in netCDF format as these foundational products are primarily intended for long-term scientific archiving. Most users are expected to utilize L1C and L2-L4 products in the map-projected (gridded) COG format in 110x110km sub-image tiles (UTM projection).

#### 2.1.2. COG Format**

Analysis-ready SBG products are distributed in a gridded and tiled form using the COG (Cloud Optimized GeoTiff) format [[https://www.cogeo.org/]{.underline}](https://www.cogeo.org/). While COG files are typically larger than regular GeoTIFF files, they have the ability to adjust viewing scales and more efficiently stream only the required portions of an image file. COG files use the same ".tif" suffix as regular GeoTiff files.

L3 ETF files are COG-formatted image sub-tiles based on a modified form of the Military Grid Reference System (MGRS) tiling scheme as defined by NASA ([[https://hls.gsfc.nasa.gov/products-description/tiling-system/]{.underline}](https://hls.gsfc.nasa.gov/products-description/tiling-system/)) and the ESA Sentinel-2 UTM grid ([[https://eatlas.org.au/data/uuid/f7468d15-12be-4e3f-a246-b2882a324f59]{.underline}](https://eatlas.org.au/data/uuid/f7468d15-12be-4e3f-a246-b2882a324f59)). These tiles divide Universal Transverse Mercator (UTM) zones into square tiles 109760 m across, using a 60m cell size with 1800 rows by 1800 columns, totaling 3.24 million pixels per tile. This allows the end user to assume that each 60 meter SBG pixel will remain in the same location at each timestep observed in analysis. The COG format also facilitates end-user analysis as a universally recognized and supported format, compatible with open-source software, including QGIS, ArcGIS, GDAL, the Raster package in R, rioxarray in Python, and Rasters.jl in Julia.

Each SBG gridded or tiled COG product additionally contains a rendered browse image in GeoJPEG format with a .jpeg extension. This image format is universally recognized and supported, and the files are compatible with Google Earth. Each collection of tiled files also includes a separate .json file containing the Product Metadata and Standard Metadata in JSON format for the parent image granule.

## 3. [SBG-TIR PRODUCT FILES]{.smallcaps}

The SBG-TIR product file will contain at least 3 groups of data: A standard metadata group that specifies the same type of contents for all products, a product specific metadata group that specifies those metadata elements that are useful for defining attributes of the product data, and the group(s) containing the product data. (Note: A product metadata is not to be confused with a GeoTIFF object metadata.)

All product file names will have the form:

\<SBG_Name\>\_\<PROD_TYPE\>\_\<OOOOO\>\_\<SSS\>\_\<YYYYMMDDThhmmss\>\_\<BBbb\>\_\<VV\>.\<TYPE\>

Where:

SBG_Name: SBG-TIR name designation (TBD)

PROD_TYPE: Example=L3_ETF

OOOOO: Orbit number; starting at start of mission, ascending equatorial crossing

SSS: Scene ID; starting at first scene of each orbit

YYYYMMDD: Year, month, day of scene start time

hhmmss: Hour, minute, second of scene start time

BBbb: Build ID of software that generated product, Major+Minor (2+2 digits)

VV: Product version number (2 digits)

TYPE: File type extension=

tif for the data file

tif.met for the metadata file.

### 3.1. Standard Metadata

This is the minimal set of metadata that must be included with each product file. The standard metadata consists of the following:


| **Name** | **Type** | **Size** | **Example** |
| --- | --- | --- | --- |
| AncillaryInputPointer | String | variable | Group name of ancillary file list | 
| AutomaticQualityFlag | String | variable | PASS/FAIL (of product data) |
| BuildId | String | variable | |
| CollectionLabel | String | variable | |
| DataFormatType | String | variable | NCSAHDF5 |
| DayNightFlag | String | variable | |
| EastBoundingCoordinate | LongFloat | 8 | |
| HDFVersionId | String | variable | 1.8.16 |
| ImageLines | Int32 | 4 | 5632 |
| ImageLineSpacing | Float32 | 4 | 68.754 | 
| ImagePixels | Int32 | 4 | 5400 |
| ImagePixelSpacing | Float32 | 4 | 65.536 |
| InputPointer | String | variable | |
| InstrumentShortName | String | variable | SBG |
| LocalGranuleID | String | variable | --- |
| LongName | String | variable | SBG |
| InstrumentShortName | String | variable | --- |
| LocalGranuleID | String | variable | --- |
| LongName | String | variable | SBG |
| NorthBoundingCoordinate | LongFloat | 8 | --- |
| PGEName | String | variable | L2_LSTE (L2_CLOUD) |
| PGEVersion | String | variable | |
| PlatformLongName | String | variable | |
| PlatformShortName | String | variable | |
| PlatformType | String | variable | Spacecraft |
| ProcessingLevelID | String | variable | 1 |
| ProcessingLevelDescription | String | variable | Level 2 Land Surface Temperatures and Emissivity (Level 2 Cloud mask) |
| ProducerAgency | String | variable | JPL |
| ProducerInstitution | String | variable | Caltech |
| ProductionDateTime | String | variable | |
| ProductionLocation | String | variable | |
| CampaignShortName | String | variable | Primary |
| RangeBeginningDate | String | variable | |
| CampaignShortName | String | variable | |
| RangeBeginningDate | String | variable | |
| RangeBeginningTime | String | variable | |
| RangeEndingDate | String | variable | |
| RangeEndingTime | String | variable | |
| SceneID | String | variable | |
| ShortName | String | variable | L2_LSTE (L2_CLOUD) |
| SceneID | String | variable | |
| ShortName | String | variable | |
| SISName | String | variable | |
| SISVersion | String | variable | |
| SouthBoundingCoordinate | LongFloat | 8 | |
| StartOrbitNumber | String | variable | |
| StartOrbitNumber | String | variable | |
| WestBoundingCoordinate | LongFloat | 8 | |

*Table 3-1: Standard Product Metadata*
### 3.2. Product-Specific Metadata

Any additional metadata necessary for describing the product will be recorded in this group.

Table 3-2: Product Specific Metadata

  ------------------------ --------------------- ---------- ------------------------------
  **Name**                 **Type**              **Size**   **Example**

  **Group**                **L3_ETF_Metadata**              

  Background_temp          Float                 4          

  ETF Detections           Int8                             0 or 1

  Overall_quality          Int16                 2          
  ------------------------ --------------------- ---------- ------------------------------

## 3.3. Product Data

The product data will be stored in this group. Exact contents and layouts to be defined by each PGE and will conform to the GeoTIFF specifications.

Table 3-3: Product Data Definitions

  ------------------------ -------------------------------------- ---------- ------------------------------
  **Field Name**           **TYPE**                               **UNIT**   **Field Data**

  **GROUP**                **L3_ELEVATED_TEMPERATURE_FEATURES**              

  ETF Detections           Int8                                   None       0 or 1

  ETF Temperatures         Float                                  Kelvin     

  Global Accuracy          Float                                  None       

  DataQuality              Int8                                   None       
  ------------------------ -------------------------------------- ---------- ------------------------------

## 3.4. Product Metadata File

The product metadata for each product file will be generated by the PCS from the metadata contents of each product file. The metadata will be converted into extensible markup language (XML). These will be used by the DAAC for cataloging. Exact contents and layout to be defined by PCS.
