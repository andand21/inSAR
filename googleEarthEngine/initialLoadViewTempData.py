#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:39:55 2026

@author: aidanturner
"""
import ee
import geemap
import ipyleaflet


ee.Authenticate()

# Initialize the Earth Engine module.
ee.Initialize(project='climateexperiment20260302')

first_image = ee.Image( 'LANDSAT/LT05/C02/T1_L2/LT05_118038_20000606')

# Initialize a map object.
m = geemap.Map()

# Add the image to the map.
m.add_layer(first_image, None, 'Random image')

# Display the map (you can call the object directly if it is the final line).
m

n = ipyleaflet.Map()
n

#1pm 5th May Warren Rooms