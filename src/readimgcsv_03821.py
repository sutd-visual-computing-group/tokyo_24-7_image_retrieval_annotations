# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:38:58 2020

@author: jem_n
"""

import os
import numpy as np
import pandas as pd
import csv

path = 'D:\\User Folders\\Downloads HDD\\247dataset_googlestreetview\\03821'

coords_list = []

for dirname, directory, list_of_filenames in os.walk(path):
    for filename in list_of_filenames:
        if '.csv' in filename:
            with open(dirname+'\\'+filename) as csvfile:
                content = csv.reader(csvfile)
                for row in content:
                    imptcontent = [filename,row[0],row[1],row[-2],row[-1]]
                    coords_list.append(imptcontent)
                
coords_df = pd.DataFrame(coords_list)
coords_df.to_csv('imginfo_03821.csv')