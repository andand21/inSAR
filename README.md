# inSAR
inSAR Remote Sensing Analysis Project

Overview:</br>
Project to refresh previous inSAR analysis. Using recent paper (Walwer et al 2025 [1]) as a baseline, using data from the paper: https://zenodo.org/records/12752832
Data from study is post processed as described in [3]. Downloading some data to practice some preprocessing.
Doing +/-0.03 minutes Lat Lon around Pacaya Volcano - Registering to get data from [3] takes a couple of days and needs an institutional email
14.32-14.39 to -90.64 - -90.57

Continuous measurement of small lava flows requries significant amount of data. Mozambique flooding may be an easier comparison to try with more limited data collection. [4]

Using google earth engine for climate analysis - Cloud-Based Remote Sensing with Google Earth Engine [5]. Gives details on using google earth engine for remote sensing through a series of labs
Journal of remote sensing for enviroment - has a paper on defining war torn damage based on SENTIEL-1 data from within google earth engine [6]
Paper on how to remotely sense for early drought indicators and impacts on crops yield, risking famine [7]


Import:</br>
Testing out inSARdev python. Limited on data storage to check raw data from https://search.asf.alaska.edu/#/?zoom=10.523&center=-90.639,14.243&polygon=POLYGON((-90.64%2014.32,-90.57%2014.32,-90.57%2014.39,-90.64%2014.39,-90.64%2014.32))&beamModes=IW&polarizations=VV%2BVH&flightDirs=Ascending&subtypes=SA&resultsLoaded=true&granule=S1A_IW_GRDH_1SDV_20250219T001440_20250219T001505_057958_072701_B1F4-METADATA_GRD_HD.

Will need some more temporary data space, as only need small amount of area from images.


Preprocessing:</br>
Already done on dataset I have. Aim to download and analyse that data later.


Processing:</br>
Import images - review variations between the interferometery


Presentation:</br>
For testing post processing compare to [1] dataset. Key lava flows at set points in time.


References:</br>
[1] D Walwer, J Gonzalez-Santana, C Wauthier, E Calais, M Ghil, Multichannel singular spectrum analysis (M-SSA) of InSAR data sets: data-adaptive interpolation and decomposition of Sentinel-1 time-series at Pacaya Volcano, Guatemala, Geophysical Journal International, Volume 242, Issue 3, September 2025, ggaf257, https://doi.org/10.1093/gji/ggaf257
[2] P. Berardino, G. Fornaro, R. Lanari and E. Sansosti, "A new algorithm for surface deformation monitoring based on small baseline differential SAR interferograms," in IEEE Transactions on Geoscience and Remote Sensing, vol. 40, no. 11, pp. 2375-2383, Nov. 2002, doi: 10.1109/TGRS.2002.803792.
[3] Judit Gonzalez-Santana, Christelle Wauthier, Unraveling long-term volcano flank instability at Pacaya Volcano, Guatemala, using satellite geodesy, Journal of Volcanology and Geothermal Research, Volume 410, 2021, 107147, ISSN 0377-0273,https://doi.org/10.1016/j.jvolgeores.2020.107147.
[4] https://www.amnesty.org/en/latest/campaigns/2026/02/trumps-anti-green-stance-leaves-mozambique-at-mercy-of-climate-crisis/
[5] Jeffrey A. Cardille, Morgan A. Crowley, David Saah, Nicholas E. Clinton, Cloud-Based Remote Sensing with Google Earth Engine https://doi.org/10.1007/978-3-031-26588-4
[6] Ollie Ballinger, Open access battle damage detection via Pixel-Wise T-Test on Sentinel-1 imagery, Remote Sensing of Environment, Volume 331, 2025, 115025, ISSN 0034-4257, https://doi.org/10.1016/j.rse.2025.115025. (https://www.sciencedirect.com/science/article/pii/S0034425725004298)
[7] Martha C. Anderson, Cornelio A. Zolin, Paulo C. Sentelhas, Christopher R. Hain, Kathryn Semmens, M. Tugrul Yilmaz, Feng Gao, Jason A. Otkin, Robert Tetrault, The Evaporative Stress Index as an indicator of agricultural drought in Brazil: An assessment based on crop yield impacts, Remote Sensing of Environment, Volume 174, 2016, Pages 82-99, ISSN 0034-4257, https://doi.org/10.1016/j.rse.2015.11.034. (https://www.sciencedirect.com/science/article/pii/S0034425715302212)