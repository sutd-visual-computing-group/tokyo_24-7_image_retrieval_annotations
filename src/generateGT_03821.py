# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:04:01 2020

@author: jem_n
"""

import os
import numpy as np
import pandas as pd
import csv

query_csv_path = 'D:\\User Folders\\Downloads HDD\\247query_subset_v2\\247query_03821\\queryinfo_03821.csv'
image_csv_path = 'D:\\User Folders\\Downloads HDD\\247dataset_googlestreetview\\03821\\imginfo_03821.csv'
groundtruth_path = 'D:\\User Folders\\Downloads HDD\\247_groundtruths\\03821'

def skipqueries(index):
    if index % 2 == 0:
        return False
    return True

def skipimages(index):
    if index % 12 == 0:
        return False
    return True

query_df = pd.read_csv(query_csv_path,index_col=1)#,skiprows=lambda x: skipqueries(x))
image_df = pd.read_csv(image_csv_path,index_col=1)#,skiprows=lambda x: skipimages(x))

matching_tuple = {}

for index, row in query_df.iterrows():
    easting = row[3]
    northing = row[4]
    list_of_matches = []
    for index2, row2 in image_df.iterrows():
        easting2 = row2[3]
        northing2 = row2[4]
        if np.sqrt((easting-easting2)**2+(northing-northing2)**2) <= 25:
            list_of_matches.append(index2)
    matching_tuple[index] = list_of_matches

for key in matching_tuple:
    path = os.path.join(groundtruth_path,'{}.txt'.format(key.replace('.jpg','')))
    with open(path,'w') as f:
        for item in matching_tuple[key]:
            item = item.replace('.csv','\n')
            f.write(item)
        
        