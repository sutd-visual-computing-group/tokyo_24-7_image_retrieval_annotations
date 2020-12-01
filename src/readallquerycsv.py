# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:38:58 2020

@author: jem_n
"""

import os
import numpy as np
import pandas as pd
import csv

path = 'D:\\User Folders\\Downloads HDD\\247query_subset_v2'

coords_list = []

for dirname, _, list_of_filenames in os.walk(path):
    for filename in list_of_filenames:
        if '.csv' in filename:
            with open(filename) as csvfile:
                content = csv.reader(csvfile)
                for row in content:
                    imptcontent = [row[0],row[1],row[2],row[-2],row[-1]]
                    coords_list.append(imptcontent)
                    
coords_df = pd.DataFrame(coords_list)
coords_df.to_csv('output.csv')