# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:39:11 2018

@author: Shalini
"""
import numpy as np
#data_set = np.loadtxt("gradients.rnk",delimiter='\t')
import csv 


dictlist = [dict() for x in range(399)]

key = []
rank = []
with open('gradients.rnk','r') as csvfile: 
    reader = csv.reader(csvfile, delimiter='\t') 
    for row in reader:
        key.append(row[0])
        rank.append(row[1])
d = {}
for i in range(0,399):
    dictlist[i]['Feature'] = key[i]
    dictlist[i]['Rank'] = rank[i]
    d[key[i]] = rank[i]
