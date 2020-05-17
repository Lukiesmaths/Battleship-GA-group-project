# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:42:11 2020

@author: Luke
"""
import numpy as np
import random
ab = 1
wy = 1

initialpop = np.zeros((100,20))


for i in range(0,100):
    for j in range(0,10):
        initialpop[i][j] = random.gauss(0,ab)
    for j in range(10,20):
        initialpop[i][j] = random.gauss(0,wy)
        