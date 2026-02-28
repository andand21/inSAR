#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:42:37 2026

@author: aidanturner
"""
import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

SBASFileName =  '/Users/aidanturner/Downloads/M-SSA_InSAR_Repo/data/InSAR/S1_OPOD_asc_allorbit_to122020_clean/MSBAS_260_229_5_5.txt'

#SBAS - Load check out what pairs work best
metaData = pd.read_csv(SBASFileName,sep=' ',header=None)
metaData.columns = ["FileName","Time","Lat","Lon"]

x = range(1,metaData.shape[0]+1)
# plt.scatter(x,metaData[["Time"]])
# plt.show()
# plt.scatter(x,metaData[["Lat"]])
# plt.show()
# plt.scatter(x,metaData[["Lon"]])
# plt.show()
# plt.scatter(metaData[["Lat"]],metaData[["Lon"]])
# plt.show()


latLonScaled = metaData[["Lat","Lon"]].copy()
timeScaled = metaData[["Time"]].copy()

for column in latLonScaled.columns:
     latLonScaled[column] = latLonScaled[column] / latLonScaled[column].abs().max()
timeScaled = timeScaled / timeScaled.abs().max()

#SBAS find pairs that are close temporally and spatially
#Normalise?
#for each file - take it away from all the others - find rms of the closest one
latLonScaled = timeScaled.to_numpy()
spatialDist = cdist(spatialData, spatialData)

# spatialData2 = metaData[["Time","Lat","Lon"]].to_numpy()
# spatialDist2 = cdist(spatialData2, spatialData2)

np.min(spatialDist,axis=0)
np.unravel_index(spatialDist.argmin(),spatialDist.shape)

minVal = []
minLoc = []

rows= [0,86,128]
pd.DataFrame(spatialDist).to_csv('Test.csv')
#for row in range(spatialDist.shape[0]):
for row in rows:

    minVal += [spatialDist[np.nonzero(spatialDist[:,row]),row].min()]
    if row in minLoc:
        minLoc += [minLoc.index(row)]
    else:
        minIdx = spatialDist[np.nonzero(spatialDist[:,row]),row].argmin()
        if minIdx < row:
            minLoc += [minIdx]
        else:
            minLoc += [minIdx + 1]
    
    
  
    #check why no equal pair - length of set =/= length of data
# countNum = []
# minValuePairs = []
# for idx in range(218):
#     temp = 0
#     for i in range(len(minLoc)):
#         if idx == minLoc[i]:
#             temp += 1
#             minValuePair = [minVal[i],minVal[idx]]
#     countNum.append(temp)
#     minValuePairs.append(minValuePair)
# plt.plot(range(218),countNum)
# plt.show()
# numberSamples = spatialData.shape[0]
# il1 = np.tril_indices(numberSamples, k=-1)
# dist = spatialDist[il1]
# arg_min = dist.argmin()
# min = dist.min()
#Import Data
# Two images and compare? Multiple ses?
# Preprocessing - reducing noise? Stacking of mutliple images?
# Process
# Box car method?
# Present - broad images initally - can build
