#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:42:37 2026

@author: aidanturner
"""
import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform
import matplotlib.pyplot as plt
   
# Example dataframe
# df = pd.DataFrame({
#     "lat": [...],
#     "lon": [...],
#     "time": [...]  # datetime or timestamp
# })

def unique_closest_pairs(df, time_scale=1e-6):
    # Convert time to seconds
    t = pd.to_datetime(df["time"]).astype("int64") // 1_000_000_000

    # Build feature matrix
    X = np.column_stack([
        df["lat"].values,
        df["lon"].values,
        t * time_scale
    ])

    # Pairwise distances
    D = squareform(pdist(X))
    np.fill_diagonal(D, np.inf)

    # For each row, find nearest neighbour
    nearest_idx = np.argmin(D, axis=1)
    nearest_dist = D[np.arange(len(D)), nearest_idx]

    # Build unique pairs
    pairs = set()
    for i, j in enumerate(nearest_idx):
        a, b = sorted((i, j))
        pairs.add((a, b))

    # Convert to list with distances
    unique_pairs = []
    for a, b in pairs:
        unique_pairs.append({
            "row1": a,
            "row2": b,
            "distance": D[a, b]
        })

    # RMS of distances
    distances = np.array([p["distance"] for p in unique_pairs])
    rms = np.sqrt(np.mean(distances**2))

    return {
        "pairs": unique_pairs,
        "rms": rms
    }

def unique_pairs_lat_only(df):
    df.sort("lat")

def plot_metaData(metaData):
    x = range(1,metaData.shape[0]+1)
    plt.scatter(x,metaData[["time"]])
    plt.show()
    plt.scatter(x,metaData[["lat"]])
    plt.show()
    plt.scatter(x,metaData[["lon"]])
    plt.show()
    plt.scatter(metaData[["lon"]],metaData[["lat"]])
    plt.show()

if __name__ == '__main__':
    SBASFileName =  '/Users/aidanturner/Downloads/M-SSA_InSAR_Repo/data/InSAR/S1_OPOD_asc_allorbit_to122020_clean/MSBAS_260_229_5_5.txt'

    #SBAS - Load check out what pairs work best
    metaData = pd.read_csv(SBASFileName,sep=' ',header=None)
    metaData.columns = ["FileName","time","lat","lon"]

    # plt raw meta data
    # plot_metaData(metaData)
    
    # unique paris - distance of lat/lon/time:
    # result = unique_closest_pairs(metaData)
    
    # lat/lon fairly continuos - sort by lat only
    #TODO generalise sortingß
    metaData.sort_values("lat")
    
    
    
