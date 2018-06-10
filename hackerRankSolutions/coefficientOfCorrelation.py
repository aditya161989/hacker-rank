# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:38:12 2018

@author: I068237
"""

import numpy as np
import re

#n = int(input())
#print("Enter scores in physics")
arr = input()
arr = re.sub('\s+',' ',arr)
physics = list(map(int,arr.split(' ')))

#print("Enter scores in history")
arr = input()
arr = re.sub('\s+',' ',arr)
history = list(map(int,arr.split(' ')))

phy_sd = np.std(physics)
hist_sd = np.std(history)

p_temp = physics - np.mean(physics)
h_temp = history - np.mean(history)

covariance = np.dot(p_temp.transpose(), h_temp)

coc = covariance/(phy_sd*hist_sd)

print(coc)