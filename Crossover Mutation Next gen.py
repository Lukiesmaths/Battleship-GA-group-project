# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:27:57 2020

@author: Luke
"""

#a basic crossover and mutation operator, the crossover will need to be changed for an fft.
import numpy as np
import random
from random import sample
sz = 100 #size of population
ab = 2 #interval size [-ab, ab] that alpha and beta are between
wy = 1/50 #same as above for mew and omega
crossabs = 4 #number of genes crossed over for ab
crosswys = 4 #above for wy


genone = np.zeros((sz,40))
for i in range(0,sz):
    for j in range(0,20):
        genone[i][j] = random.gauss(0,ab)
    for j in range(20,40):
        genone[i][j] = random.gauss(0,wy)
points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]


examplescores = np.random.rand(1,sz)
def newgeneration(arr):
    newgene = np.zeros((sz,40))
    order = ((-arr).argsort(axis=-1)[:, :sz] ) #sorts the scores
    for i in range(0,11): #10 best genes go through unchanged
        newgene[i,:] = genone[order[:,i],:]
    i = 10
    for rep1 in range(0,9): #45 genes have replication only #first 10 genes as partner
        for rep2 in range(rep1+1,10): #
                #crosspoints = np.random.randint(0,high = 21, size = 10)
                newgene[i,:] = newgene[rep1,:]
                #newgene[i,2] = newgene[rep2,2]#need to find way to get swap points properly!
                crosspoints = sample(points,10)
                for swaps in range(0,10):
                   
                    newgene[i,crosspoints[swaps]] = newgene[rep2,crosspoints[swaps]]
                i = i+1
   
    #same as above + mutation
    #mutationpoints = [a, b, c, d, ...]
    #newgene[i,mutationpoint]
    i = 55
    for rep1 in range(0,9): #45 genes have replication only #first 10 genes as partner
        for rep2 in range(rep1+1,10): #
                #crosspoints = np.random.randint(0,high = 21, size = 10)
                newgene[i,:] = newgene[rep1,:]
                #newgene[i,2] = newgene[rep2,2]#need to find way to get swap points properly!
                crosspoints = sample(points,10)
                mutationpoints = sample(points,5)
                print(mutationpoints)
                for swaps in range(0,10):
                   
                    newgene[i,crosspoints[swaps]] = newgene[rep2,crosspoints[swaps]]
               
                for mutations in range(0,5):
                   
                   newgene[i,mutationpoints[mutations]] = random.gauss(0,ab)
                i = i+1
   
    return(newgene)