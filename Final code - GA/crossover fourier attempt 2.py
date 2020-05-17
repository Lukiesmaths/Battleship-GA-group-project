# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:05:11 2020

https://stackoverflow.com/questions/4258106/how-to-calculate-a-fourier-series-in-numpy
"""
#tried using https://stackoverflow.com/questions/4258106/how-to-calculate-a-fourier-series-in-numpy and sympi to get crossover to work, unfortunately no sucsess

import numpy as np
samplingFrequency   = 100;
samplingInterval       = 1 / samplingFrequency;
beginTime           = 0;
endTime             = 100; 
import random
ab = 1
wy = 1
import matplotlib.pyplot as plotter
import sympy as sy
initialpop = np.zeros((100,20))
from sympy.abc import x
from sympy import sin,pi,cos
for i in range(0,100):
    for j in range(0,10):
        initialpop[i][j] = random.gauss(0,ab)
    for j in range(10,20):
        initialpop[i][j] = random.gauss(0,wy)
        
        
def fourier_series_coeff_numpy(f, T, N, return_complex=False):
    """Calculates the first 2*N+1 Fourier series coeff. of a periodic function.

    Given a periodic, function f(t) with period T, this function returns the
    coefficients a0, {a1,a2,...},{b1,b2,...} such that:

    f(t) ~= a0/2+ sum_{k=1}^{N} ( a_k*cos(2*pi*k*t/T) + b_k*sin(2*pi*k*t/T) )

    If return_complex is set to True, it returns instead the coefficients
    {c0,c1,c2,...}
    such that:

    f(t) ~= sum_{k=-N}^{N} c_k * exp(i*2*pi*k*t/T)

    where we define c_{-n} = complex_conjugate(c_{n})

    Refer to wikipedia for the relation between the real-valued and complex
    valued coeffs at http://en.wikipedia.org/wiki/Fourier_series.

    Parameters
    ----------
    f : the periodic function, a callable like f(t)
    T : the period of the function f, so that f(0)==f(T)
    N_max : the function will return the first N_max + 1 Fourier coeff.

    Returns
    -------
    if return_complex == False, the function returns:

    a0 : float
    a,b : numpy float arrays describing respectively the cosine and sine coeff.

    if return_complex == True, the function returns:

    c : numpy 1-dimensional complex-valued array of size N+1

    """
    # From Shanon theoreom we must use a sampling freq. larger than the maximum
    # frequency you want to catch in the signal.
    f_sample = 2 * N
    # we also need to use an integer sampling frequency, or the
    # points will not be equispaced between 0 and 1. We then add +2 to f_sample
    t, dt = np.linspace(0, T, f_sample + 2, endpoint=False, retstep=True)

    y = np.fft.rfft(f(t)) / t.size

    if return_complex:
        return y
    else:
        y *= 2
        return y[0].real, y[1:-1].real, -y[1:-1].imag        





def crossover(gen1, gen2):
    signalfreqsin = np.zeros((10,1))
    signalfreqcos = np.zeros((10,1))
    Amplitudesin = np.zeros((10,1))
    Amplitudecos = np.zeros((10,1))

    
    
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
    amplitude = x*0
    for i in range(0,10):
        amplitude = Amplitudesin[i]*sy.sin(signalfreqsin[i]*x) + amplitude
    for i in range(0,10):    
        amplitude = Amplitudecos[i]*sy.cos(signalfreqcos[i]*x) + amplitude
     
    amplitude = amplitude/2    
    #Z = fourier_series_coeff_numpy(amplitude, 2*np.pi, 100, return_complex=False)
    
    return amplitude





















crossover(initialpop[1],initialpop[2])
    