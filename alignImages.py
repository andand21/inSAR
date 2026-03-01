#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:30:15 2026

@author: aidanturner
"""
# test images - located in similar positions - minimal lat variation
#20150425T001341
#20150519T001341

import matplotlib.pyplot as plt
from skimage import io
#check alignment as pre processing might have done a chunk of the work

loading_directory = "/Users/aidanturner/Downloads/M-SSA_InSAR_Repo/data/InSAR/S1_OPOD_asc_allorbit_to122020_clean"

file1 = "MSBAS_20150425T001341_LOS.tif"
file2 = "MSBAS_20150519T001341_LOS.tif"

I1 = io.imread(loading_directory+"/"+file1)

I2 = io.imread(loading_directory+"/"+file2)

I3 = I1 + I2

fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3), ncols=3)

# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos1 = ax1.imshow(I1, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which Axes object it should be near

pos2 = ax2.imshow(I2, cmap='Blues', interpolation='none')

pos3 = ax3.imshow(I3, cmap='Blues', interpolation='none')


fig.colorbar(pos1, ax=ax1)

fig.colorbar(pos2, ax=ax2)

fig.colorbar(pos3, ax=ax3)

