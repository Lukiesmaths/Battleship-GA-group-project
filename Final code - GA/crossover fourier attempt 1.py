# -*- coding: utf-8 -*-
"""
Created on Tue May  5 20:08:16 2020


"""
# using code from https://pythontic.com/visualization/signals/fouriertransform_fft to try and get crossover to work, unfortunately did not give correct output
import numpy as np
samplingFrequency   = 100;
samplingInterval       = 1 / samplingFrequency;
beginTime           = 0;
endTime             = 100; 
import random
ab = 1
wy = 1
import matplotlib.pyplot as plotter




def crossover(gen1, gen2):
    signalfreqsin = np.zeros((10,1))
    signalfreqcos = np.zeros((10,1))
    Amplitudesin = np.zeros((10,1))
    Amplitudecos = np.zeros((10,1))
    time        = np.arange(beginTime, endTime, samplingInterval);
    amplitude = 0.0
    
    
    for i in  range(0,5):
        signalfreqsin[i] = gen1[i+10]
        signalfreqcos[i] = gen1[i+15]
        Amplitudesin[i] = gen1[i]
        Amplitudecos[i] = gen1[i+5]
    for i in range(5,10):
        signalfreqsin[i] = gen2[i+5]
        signalfreqcos[i] = gen2[i+10]
        Amplitudesin[i] = gen2[i-5]
        Amplitudecos[i] = gen2[i]
    
    for i in range(0,10):
        amplitude = Amplitudesin[i]*np.sin(2*np.pi*signalfreqsin[i]*time) + amplitude
    for i in range(0,10):    
         amplitude = Amplitudecos[i]*np.cos(2*np.pi*signalfreqcos[i]*time) + amplitude
     
    amplitude = amplitude/2    
    fourierTransform = np.fft.fft(amplitude)/len(amplitude)         # Normalize amplitude
    fourierTransform = fourierTransform[range(int(len(amplitude)/2))]



    
    

    np.amax(abs(fourierTransform))

    
#    Z = np.argpartition(A,-4)[-6:]
    figure, axis = plotter.subplots(4, 1)

    plotter.subplots_adjust(hspace=1)
    tpCount     = len(amplitude)

    values      = np.arange(int(tpCount/2))

    timePeriod  = tpCount/samplingFrequency

    frequencies = values/timePeriod

    
    axis[3].set_title('Fourier transform depicting the frequency components')

 

    axis[3].plot(frequencies, abs(fourierTransform))

    axis[3].set_xlabel('Frequency')

    axis[3].set_ylabel('Amplitude')

    
    return fourierTransform




initialpop = np.zeros((100,20))


for i in range(0,100):
    for j in range(0,10):
        initialpop[i][j] = random.gauss(0,ab)
    for j in range(10,20):
        initialpop[i][j] = random.gauss(0,wy)
        
        
        


crossover(initialpop[1],initialpop[2])


# waveform = gen[0][i]*np.sin((gen[0][i+10])*x)+(gen[0][i+5])*np.cos((gen[0][i+15])*x) + waveform        
