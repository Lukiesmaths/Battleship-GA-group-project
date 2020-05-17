# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:00:08 2020

@author: lh1663
"""

import matplotlib.pylab as plt
import numpy as np
import random
ab = 1 #hyperparameter for the intial population
wy = 1 #hyperparameter for the intial population


genone = np.zeros((1,20)) #generate a random population to make sure it works
for j in range(0,10):
    genone[0][j] = random.gauss(0,ab) #represents the alpha and beta values
for j in range(10,20):
    genone[0][j] = random.gauss(0,wy) # represents the mu and omega values



array = np.zeros(shape = (100,2))

for i in range(0,10):
    for j in range(0,10):
        array[10*i+j] = [i,j] #set up board array
       
       
   
   
   
   
def waveform(gen,x): #creates waveform of a chromosome
    waveform = 0*np.sin(x)
    for i in  range(0,5):
        waveform = gen[0][i]*np.sin((gen[0][i+10])*x)+(gen[0][i+5])*np.cos((gen[0][i+15])*x) + waveform
    return waveform
print(waveform(genone,1))
print(waveform(genone,2))
x = np.linspace(0, 100, 101)
values = np.zeros((1,100)) #plot it to check it works properly, need these
for i in range(0,100):
    values[0][i] = waveform(genone,i) #find values of the sum of harmonic waves at each location on grid
aimorder = np.flip(np.argsort(values)) #sort these values into an order
plt.plot(x,waveform(genone,x)) #plot to check it works
origaimorder = np.flip(np.argsort(values)) #get an aimorder to use in placement

array = np.zeros(shape = (110,2))

for i in range(0,10):
    for j in range(0,10):
        array[10*i+j] = [i,j]
for i in range(0,10):        
    array[i+100] = [10,10]
       
aimorder_lin = aimorder.reshape(-1)  
origaimorder_lin = origaimorder.reshape(-1)  
grid = np.zeros((10,10))
gridf = np.zeros((10,10))    
grid_lin = grid.reshape(-1)  


oneship = np.zeros(shape = (1,2)) #don't actually need this for our Battleship, can be edited out
twoship = np.zeros(shape = (2,2))
threeship = np.zeros(shape = (3,2))
threeship2 = np.zeros(shape = (3,2))
fourship = np.zeros(shape = (4,2))
fiveship = np.zeros(shape = (5,2))
loc = np.zeros((2,6)) #make it 2,5 when not using one length ship

for i in range(0,100): #for each grid on the graph we go through and plot them on a test grid until a ship of the right length is formed
    vec = np.zeros([10,5]) #need a way to evaluate which ship has the lowest values
    grid_lin[int(aimorder_lin[i])] = i+1 #place number of shot on a grid

    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0 and 10 > array[int(aimorder_lin[i])][1]+3 >= 0 and 10 > array[int(aimorder_lin[i])][1]+4 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0 and grid_lin[int(aimorder_lin[i])+3] != 0 and grid_lin[int(aimorder_lin[i])+4] != 0:
            vec[0][0] = grid_lin[int(aimorder_lin[i])]
            vec[0][1] = grid_lin[int(aimorder_lin[i])+1] #for each of these points we check all given direction, in this block we 
            vec[0][2] = grid_lin[int(aimorder_lin[i])+2] #check to see if placing the ith square has 4 squares filled next to it
            vec[0][3] = grid_lin[int(aimorder_lin[i])+3] #if so we save these values to vec in case there are any more ships made at
            vec[0][4] = grid_lin[int(aimorder_lin[i])+4] #the same time, if so we take the smaller values of vec
            print("place ship at")
            print([int(aimorder_lin[i])]) #this was just for testing and can be removed in the final version to speed up time
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            print([int(aimorder_lin[i])+3])
            print([int(aimorder_lin[i])+4])
            
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0 and 10 > array[int(aimorder_lin[i])][1]+3 >= 0 and 10 > array[int(aimorder_lin[i])][1]-1 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0 and grid_lin[int(aimorder_lin[i])+3] != 0 and grid_lin[int(aimorder_lin[i])-1] != 0:
            vec[1][0] = grid_lin[int(aimorder_lin[i])]
            vec[1][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[1][2] = grid_lin[int(aimorder_lin[i])+2]
            vec[1][3] = grid_lin[int(aimorder_lin[i])+3]
            vec[1][4] = grid_lin[int(aimorder_lin[i])-1]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            print([int(aimorder_lin[i])+3])
            print([int(aimorder_lin[i])-1])

    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0 and 10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]-2 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0 and grid_lin[int(aimorder_lin[i])-1] != 0 and grid_lin[int(aimorder_lin[i])-2] != 0:
            vec[2][0] = grid_lin[int(aimorder_lin[i])]
            vec[2][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[2][2] = grid_lin[int(aimorder_lin[i])+2]
            vec[2][3] = grid_lin[int(aimorder_lin[i])-1]
            vec[2][4] = grid_lin[int(aimorder_lin[i])-2]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])

    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]-2 >= 0 and 10 > array[int(aimorder_lin[i])][1]-3 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])-1] != 0 and grid_lin[int(aimorder_lin[i])-2] != 0 and grid_lin[int(aimorder_lin[i])-3] != 0:
            vec[3][0] = grid_lin[int(aimorder_lin[i])]
            vec[3][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[3][2] = grid_lin[int(aimorder_lin[i])-1]
            vec[3][3] = grid_lin[int(aimorder_lin[i])-2]
            vec[3][4] = grid_lin[int(aimorder_lin[i])-3]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])
            print([int(aimorder_lin[i])-3])

    if 10 > array[int(aimorder_lin[i])][1]-1 >= 0 and  10 > array[int(aimorder_lin[i])][1]-2 >= 0 and 10 > array[int(aimorder_lin[i])][1]-3 >= 0 and 10 > array[int(aimorder_lin[i])][1]-4 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])-1] and grid_lin[int(aimorder_lin[i])-2] != 0 and grid_lin[int(aimorder_lin[i])-3] != 0 and grid_lin[int(aimorder_lin[i])-4] != 0:
            vec[4][0] = grid_lin[int(aimorder_lin[i])]
            vec[4][1] = grid_lin[int(aimorder_lin[i])-1]
            vec[4][2] = grid_lin[int(aimorder_lin[i])-2]
            vec[4][3] = grid_lin[int(aimorder_lin[i])-3]
            vec[4][4] = grid_lin[int(aimorder_lin[i])-4]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])
            print([int(aimorder_lin[i])-3])
            print([int(aimorder_lin[i])-4])

    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0 and 10 > array[int(aimorder_lin[i])][0]+3 >= 0 and 10 > array[int(aimorder_lin[i])][0]+4 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])+20] and grid_lin[int(aimorder_lin[i])+30] != 0 and grid_lin[int(aimorder_lin[i])+40] != 0:
            vec[5][0] = grid_lin[int(aimorder_lin[i])]
            vec[5][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[5][2] = grid_lin[int(aimorder_lin[i])+20]
            vec[5][3] = grid_lin[int(aimorder_lin[i])+30]
            vec[5][4] = grid_lin[int(aimorder_lin[i])+40]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
            print([int(aimorder_lin[i])+30])
            print([int(aimorder_lin[i])+40])

    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0 and 10 > array[int(aimorder_lin[i])][0]+3 >= 0 and 10 > array[int(aimorder_lin[i])][0]-1 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])+20] and grid_lin[int(aimorder_lin[i])+30] != 0 and grid_lin[int(aimorder_lin[i])-10] != 0:
            vec[6][0] = grid_lin[int(aimorder_lin[i])]
            vec[6][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[6][2] = grid_lin[int(aimorder_lin[i])+20]
            vec[6][3] = grid_lin[int(aimorder_lin[i])+30]
            vec[6][4] = grid_lin[int(aimorder_lin[i])-10]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
            print([int(aimorder_lin[i])+30])
            print([int(aimorder_lin[i])-10])

    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0 and 10 > array[int(aimorder_lin[i])][0]-1 >= 0 and 10 > array[int(aimorder_lin[i])][0]-2 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])+20] != 0 and grid_lin[int(aimorder_lin[i])-20] != 0:
            vec[7][0] = grid_lin[int(aimorder_lin[i])]
            vec[7][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[7][2] = grid_lin[int(aimorder_lin[i])+20]
            vec[7][3] = grid_lin[int(aimorder_lin[i])-10]
            vec[7][4] = grid_lin[int(aimorder_lin[i])-20]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])

    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]-1 >= 0 and 10 > array[int(aimorder_lin[i])][0]-2 >= 0 and 10 > array[int(aimorder_lin[i])][0]-3 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] != 0 and grid_lin[int(aimorder_lin[i])-30] != 0:
            vec[8][0] = grid_lin[int(aimorder_lin[i])]
            vec[8][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[8][2] = grid_lin[int(aimorder_lin[i])-10]
            vec[8][3] = grid_lin[int(aimorder_lin[i])-20]
            vec[8][4] = grid_lin[int(aimorder_lin[i])-30]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])
            print([int(aimorder_lin[i])-30])

    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0  and 10 > array[int(aimorder_lin[i])][0]-2 >= 0 and 10 > array[int(aimorder_lin[i])][0]-3 >= 0 and 10 > array[int(aimorder_lin[i])][0]-4 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] and grid_lin[int(aimorder_lin[i])-30] != 0 and grid_lin[int(aimorder_lin[i])-40] != 0:
            vec[9][0] = grid_lin[int(aimorder_lin[i])]
            vec[9][1] = grid_lin[int(aimorder_lin[i])-10]
            vec[9][2] = grid_lin[int(aimorder_lin[i])-20]
            vec[9][3] = grid_lin[int(aimorder_lin[i])-30]
            vec[9][4] = grid_lin[int(aimorder_lin[i])-40]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])
            print([int(aimorder_lin[i])-30])
            print([int(aimorder_lin[i])-40])



    if np.any(vec) != 0: #if vec none empty, we will place a ship
        ovec = vec
        vec = vec[~np.all(vec == 0, axis=1)] #remove the empty values in vec so we are only looking at ships made
        new = vec.max(axis=1)
        new2 = np.where(new == np.min(new)) #take the one with the min value not shared
        vec2 = vec[new2]
        fiveship[0] = array[int(aimorder_lin[i])]
        fiveship[1] = array[int(aimorder_lin[int(np.amin(vec2[0][1]))-1])] #save each grid filled in
        fiveship[2] = array[int(aimorder_lin[int(np.amin(vec2[0][2]))-1])]
        fiveship[3] = array[int(aimorder_lin[int(np.amin(vec2[0][3]))-1])]
        fiveship[4] = array[int(aimorder_lin[int(np.amin(vec2[0][4]))-1])]   
        
        break
print(aimorder)
aimorder = aimorder[np.isin(aimorder,10*fiveship[0][0]+fiveship[0][1],invert = True)] #take out the ones we arent using
aimorder = aimorder[np.isin(aimorder,10*fiveship[1][0]+fiveship[1][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*fiveship[2][0]+fiveship[2][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*fiveship[3][0]+fiveship[3][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*fiveship[4][0]+fiveship[4][1],invert = True)]
aimorder_lin = aimorder.reshape(-1)  
   
grid = np.zeros((10,10))
gridf = np.zeros((10,10))    
grid_lin = grid.reshape(-1)  

































for i in range(0,95): #now for four ship and so on, same process just less checks needed as less possible ships can be made in one turn
    vec = np.zeros([8,4])
    grid_lin[int(aimorder_lin[i])] = i+1 #place number of shot on a grid
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0 and 10 > array[int(aimorder_lin[i])][1]+3 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0 and grid_lin[int(aimorder_lin[i])+3] != 0:
            
            
            
            vec[0][0] = grid_lin[int(aimorder_lin[i])]
            vec[0][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[0][2] = grid_lin[int(aimorder_lin[i])+2]
            vec[0][3] = grid_lin[int(aimorder_lin[i])+3]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            print([int(aimorder_lin[i])+3])
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0 and 10 > array[int(aimorder_lin[i])][1]-1 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0 and grid_lin[int(aimorder_lin[i])-1] != 0:
            
            
            
            vec[1][0] = grid_lin[int(aimorder_lin[i])]
            vec[1][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[1][2] = grid_lin[int(aimorder_lin[i])+2]
            vec[1][3] = grid_lin[int(aimorder_lin[i])-1]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            print([int(aimorder_lin[i])-1])
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]-2 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])-1] != 0 and grid_lin[int(aimorder_lin[i])-2] != 0:
            
            
            
            vec[2][0] = grid_lin[int(aimorder_lin[i])]
            vec[2][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[2][2] = grid_lin[int(aimorder_lin[i])-1]
            vec[2][3] = grid_lin[int(aimorder_lin[i])-2]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])
    if 10 > array[int(aimorder_lin[i])][1]-1 >= 0 and  10 > array[int(aimorder_lin[i])][1]-2 >= 0 and 10 > array[int(aimorder_lin[i])][1]-3 >= 0: #check if all right can go on
        if grid_lin[int(aimorder_lin[i])-1] and grid_lin[int(aimorder_lin[i])-2] != 0 and grid_lin[int(aimorder_lin[i])-3] != 0:
            
            
            
            vec[3][0] = grid_lin[int(aimorder_lin[i])]
            vec[3][1] = grid_lin[int(aimorder_lin[i])-1]
            vec[3][2] = grid_lin[int(aimorder_lin[i])-2]
            vec[3][3] = grid_lin[int(aimorder_lin[i])-3]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])
            print([int(aimorder_lin[i])-3])
                
            
    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0 and 10 > array[int(aimorder_lin[i])][0]+3 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])+20] and grid_lin[int(aimorder_lin[i])+30] != 0:
            vec[4][0] = grid_lin[int(aimorder_lin[i])]
            vec[4][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[4][2] = grid_lin[int(aimorder_lin[i])+20]
            vec[4][3] = grid_lin[int(aimorder_lin[i])+30]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
            print([int(aimorder_lin[i])+30])

    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0 and 10 > array[int(aimorder_lin[i])][0]-1 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])+20] and grid_lin[int(aimorder_lin[i])-10] != 0:
            vec[5][0] = grid_lin[int(aimorder_lin[i])]
            vec[5][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[5][2] = grid_lin[int(aimorder_lin[i])+20]
            vec[5][3] = grid_lin[int(aimorder_lin[i])-10]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
            print([int(aimorder_lin[i])-10])



    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]-1 >= 0 and 10 > array[int(aimorder_lin[i])][0]-2 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] != 0:
            vec[6][0] = grid_lin[int(aimorder_lin[i])]
            vec[6][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[6][2] = grid_lin[int(aimorder_lin[i])-10]
            vec[6][3] = grid_lin[int(aimorder_lin[i])-20]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])

    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0  and 10 > array[int(aimorder_lin[i])][0]-2 >= 0 and 10 > array[int(aimorder_lin[i])][0]-3 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] and grid_lin[int(aimorder_lin[i])-30] != 0:
            vec[7][0] = grid_lin[int(aimorder_lin[i])]
            vec[7][1] = grid_lin[int(aimorder_lin[i])-10]
            vec[7][2] = grid_lin[int(aimorder_lin[i])-20]
            vec[7][3] = grid_lin[int(aimorder_lin[i])-30]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])
            print([int(aimorder_lin[i])-30])


    if np.any(vec) != 0: #if vec none empty
        ovec = vec
        vec = vec[~np.all(vec == 0, axis=1)] #remove the empty
        new = vec.max(axis=1)
        new2 = np.where(new == np.min(new))
        vec2 = vec[new2]
        fourship[0] = array[int(aimorder_lin[i])]
        fourship[1] = array[int(aimorder_lin[int(np.amin(vec2[0][1]))-1])]
        fourship[2] = array[int(aimorder_lin[int(np.amin(vec2[0][2]))-1])]
        fourship[3] = array[int(aimorder_lin[int(np.amin(vec2[0][3]))-1])]
        break

aimorder = aimorder[np.isin(aimorder,10*fourship[0][0]+fourship[0][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*fourship[1][0]+fourship[1][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*fourship[2][0]+fourship[2][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*fourship[3][0]+fourship[3][1],invert = True)]
aimorder_lin = aimorder.reshape(-1)  
   
grid = np.zeros((10,10))
gridf = np.zeros((10,10))    
grid_lin = grid.reshape(-1)  





















































































for i in range(0,91):

    vec = np.zeros([6,3])
    grid_lin[int(aimorder_lin[i])] = i+1 #place number of shot on a grid
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0: #check if right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0:
            vec[0][0] = grid_lin[int(aimorder_lin[i])]
            vec[0][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[0][2] = grid_lin[int(aimorder_lin[i])+2]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            




    if  10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]-2 >= 0: #check if left can go on
        if grid_lin[int(aimorder_lin[i])-1] and grid_lin[int(aimorder_lin[i])-2] != 0:
            vec[1][0] = grid_lin[int(aimorder_lin[i])]
            vec[1][1] = grid_lin[int(aimorder_lin[i])-1]
            vec[1][2] = grid_lin[int(aimorder_lin[i])-2]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])


    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])+20] != 0:
            vec[2][0] = grid_lin[int(aimorder_lin[i])]
            vec[2][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[2][2] = grid_lin[int(aimorder_lin[i])+20]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
    
    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0 and 10 > array[int(aimorder_lin[i])][0]-2 >= 0: #check if up can go on
        if grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] != 0:
            vec[3][0] = grid_lin[int(aimorder_lin[i])]
            vec[3][1] = grid_lin[int(aimorder_lin[i])-10]
            vec[3][2] = grid_lin[int(aimorder_lin[i])-20]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])

    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+1 >= 0 : #check if up/down can go on
        if grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] != 0:
            vec[4][0] = grid_lin[int(aimorder_lin[i])]
            vec[4][1] = grid_lin[int(aimorder_lin[i])-10]
            vec[4][2] = grid_lin[int(aimorder_lin[i])+10]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])+10])

    if  10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]+1 >= 0: #check if left/right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])-1] != 0:
            vec[5][0] = grid_lin[int(aimorder_lin[i])]
            vec[5][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[5][2] = grid_lin[int(aimorder_lin[i])-1]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])-1])


    if np.any(vec) != 0: #if vec none empty
        ovec = vec
        vec = vec[~np.all(vec == 0, axis=1)] #remove the empty
        new = vec.max(axis=1)
        new2 = np.where(new == np.min(new))
        vec2 = vec[new2]
        threeship[0] = array[int(aimorder_lin[i])]
        threeship[1] = array[int(aimorder_lin[int(np.amin(vec2[0][1]))-1])]
        threeship[2] = array[int(aimorder_lin[int(np.amin(vec2[0][2]))-1])]
        
        break

aimorder = aimorder[np.isin(aimorder,10*threeship[0][0]+threeship[0][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*threeship[1][0]+threeship[1][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*threeship[2][0]+threeship[2][1],invert = True)]
aimorder_lin = aimorder.reshape(-1)  
   
grid = np.zeros((10,10))
gridf = np.zeros((10,10))    
grid_lin = grid.reshape(-1)  

for i in range(0,88):

    vec = np.zeros([6,3])
    grid_lin[int(aimorder_lin[i])] = i+1 #place number of shot on a grid
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 and  10 > array[int(aimorder_lin[i])][1]+2 >= 0: #check if right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])+2] != 0:
            vec[0][0] = grid_lin[int(aimorder_lin[i])]
            vec[0][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[0][2] = grid_lin[int(aimorder_lin[i])+2]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])+2])
            




    if  10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]-2 >= 0: #check if left can go on
        if grid_lin[int(aimorder_lin[i])-1] and grid_lin[int(aimorder_lin[i])-2] != 0:
            vec[1][0] = grid_lin[int(aimorder_lin[i])]
            vec[1][1] = grid_lin[int(aimorder_lin[i])-1]
            vec[1][2] = grid_lin[int(aimorder_lin[i])-2]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-1])
            print([int(aimorder_lin[i])-2])


    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+2 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] and grid_lin[int(aimorder_lin[i])+20] != 0:
            vec[2][0] = grid_lin[int(aimorder_lin[i])]
            vec[2][1] = grid_lin[int(aimorder_lin[i])+10]
            vec[2][2] = grid_lin[int(aimorder_lin[i])+20]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])
            print([int(aimorder_lin[i])+20])
    
    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0 and 10 > array[int(aimorder_lin[i])][0]-2 >= 0: #check if up can go on
        if grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] != 0:
            vec[3][0] = grid_lin[int(aimorder_lin[i])]
            vec[3][1] = grid_lin[int(aimorder_lin[i])-10]
            vec[3][2] = grid_lin[int(aimorder_lin[i])-20]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])-20])

    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0  and 10 > array[int(aimorder_lin[i])][0]+1 >= 0 : #check if up/down can go on
        if grid_lin[int(aimorder_lin[i])-10] and grid_lin[int(aimorder_lin[i])-20] != 0:
            vec[4][0] = grid_lin[int(aimorder_lin[i])]
            vec[4][1] = grid_lin[int(aimorder_lin[i])-10]
            vec[4][2] = grid_lin[int(aimorder_lin[i])+10]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])
            print([int(aimorder_lin[i])+10])

    if  10 > array[int(aimorder_lin[i])][1]-1 >= 0 and 10 > array[int(aimorder_lin[i])][1]+1 >= 0: #check if left/right can go on
        if grid_lin[int(aimorder_lin[i])+1] and grid_lin[int(aimorder_lin[i])-1] != 0:
            vec[5][0] = grid_lin[int(aimorder_lin[i])]
            vec[5][1] = grid_lin[int(aimorder_lin[i])+1]
            vec[5][2] = grid_lin[int(aimorder_lin[i])-1]
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
            print([int(aimorder_lin[i])-1])


    if np.any(vec) != 0: #if vec none empty
        vec = vec[~np.all(vec == 0, axis=1)] #remove the empty
        new = vec.max(axis=1)
        new2 = np.where(new == np.min(new))
        vec2 = vec[new2]
        threeship2[0] = array[int(aimorder_lin[i])]
        threeship2[1] = array[int(aimorder_lin[int(np.amin(vec2[0][1]))-1])]
        threeship2[2] = array[int(aimorder_lin[int(np.amin(vec2[0][2]))-1])]
        
        break

aimorder = aimorder[np.isin(aimorder,10*threeship2[0][0]+threeship2[0][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*threeship2[1][0]+threeship2[1][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*threeship2[2][0]+threeship2[2][1],invert = True)]
aimorder_lin = aimorder.reshape(-1)  
   
grid = np.zeros((10,10))
gridf = np.zeros((10,10))    
grid_lin = grid.reshape(-1)  




for i in range(0,79):

    vec = np.zeros([4,2])
    grid_lin[int(aimorder_lin[i])] = i+1 #place number of shot on a grid
    if 10 > array[int(aimorder_lin[i])][1]+1 >= 0 : #check if right can go on
        if grid_lin[int(aimorder_lin[i])+1]  != 0:
            vec[0][0] = grid_lin[int(aimorder_lin[i])]
            vec[0][1] = grid_lin[int(aimorder_lin[i])+1]
           
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+1])
           
    if 10 > array[int(aimorder_lin[i])][1]-1 >= 0 : #check if right can go on
        if grid_lin[int(aimorder_lin[i])-1]  != 0:
            vec[1][0] = grid_lin[int(aimorder_lin[i])]
            vec[1][1] = grid_lin[int(aimorder_lin[i])-1]
           
            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-1])
           
    if 10 > array[int(aimorder_lin[i])][0]+1 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])+10] != 0:
            vec[2][0] = grid_lin[int(aimorder_lin[i])]
            vec[2][1] = grid_lin[int(aimorder_lin[i])+10]

            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])+10])

    if 10 > array[int(aimorder_lin[i])][0]-1 >= 0: #check if down can go on
        if grid_lin[int(aimorder_lin[i])-10] != 0:
            vec[3][0] = grid_lin[int(aimorder_lin[i])]
            vec[3][1] = grid_lin[int(aimorder_lin[i])-10]

            print("place ship at")
            print([int(aimorder_lin[i])])
            print([int(aimorder_lin[i])-10])


    if np.any(vec) != 0: #if vec none empty
        vec = vec[~np.all(vec == 0, axis=1)] #remove the empty
        new = vec.max(axis=1)
        new2 = np.where(new == np.min(new))
        vec2 = vec[new2]
        twoship[0] = array[int(aimorder_lin[i])]
        twoship[1] = array[int(aimorder_lin[int(np.amin(vec2[0][1]))-1])]

        
        break

aimorder = aimorder[np.isin(aimorder,10*twoship[0][0]+twoship[0][1],invert = True)]
aimorder = aimorder[np.isin(aimorder,10*twoship[1][0]+twoship[1][1],invert = True)]


aimorder_lin = aimorder.reshape(-1)  
   
grid = np.zeros((10,10))
gridf = np.zeros((10,10))    
grid_lin = grid.reshape(-1)  

oneship[0] = array[int(aimorder_lin[0])] #can remove this is one ship is not being used
print("place ship at")
print([int(aimorder_lin[0])])

loc = np.zeros(shape = (6,2)) #want it in the form for the program
down = np.array([0,0,0,0,0], dtype=bool)



if fiveship[0][0] == fiveship[1][0]: #see which way the ship is placed
    loc[0][0] = fiveship[0][0] 
    loc[0][1] = np.amin(fiveship, axis=0)[1] #find smallest value on changing axis
    down[0] = 1
else:
    loc[0][0] = np.amin(fiveship, axis=0)[0]
    loc[0][1] = fiveship[0][1]
    down[0] = 0


if fourship[0][0] == fourship[1][0]: #same as above
    loc[1][0] = fourship[0][0]
    loc[1][1] = np.amin(fourship, axis=0)[1]
    down[1] = 1
else:
    loc[1][0] = np.amin(fourship, axis=0)[0]
    loc[1][1] = fourship[0][1]
    down[1] = 0


if threeship[0][0] == threeship[1][0]:
    loc[2][0] = threeship[0][0]
    loc[2][1] = np.amin(threeship, axis=0)[1]
    down[2] = 1
else:
    loc[2][0] = np.amin(threeship, axis=0)[0]
    loc[2][1] = threeship[0][1]
    down[2] = 0


if threeship2[0][0] == threeship2[1][0]:
    loc[3][0] = threeship2[0][0]
    loc[3][1] = np.amin(threeship2, axis=0)[1]
    down[3] = 1
else:
    loc[3][0] = np.amin(threeship2, axis=0)[0]
    loc[3][1] = threeship2[0][1]
    down[3] = 0


if twoship[0][0] == twoship[1][0]:
    loc[4][0] = twoship[0][0]
    loc[4][1] = np.amin(twoship, axis=0)[1]
    down[4] = 1
else:
    loc[4][0] = np.amin(twoship, axis=0)[0]
    loc[4][1] = twoship[0][1]
    down[4] = 0





loc[5] = oneship
















 
   