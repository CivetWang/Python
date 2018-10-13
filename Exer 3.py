# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:30:03 2017

@author: Civet
"""

import numpy as np
import pylab as py
from scipy.optimize import curve_fit
import matplotlib.pyplot as plot

def log_analysis(x,a,b):
    return a*x+b

def non_linear(x,a,b):
    return b*2**(a*x)

N,count= np.loadtxt('Cesium Radioactive Decay.txt',unpack=True)
N0,b_g=np.loadtxt('Radioactive Background 20min(20secdwell).txt', unpack=True)
N_s= count-np.average(b_g)
error=np.sqrt(count+np.average(b_g))
dt=20
N_s /= dt
t=N*20
popt1,pcov1 = curve_fit(log_analysis,t,np.log(N_s))
print(popt1)
py.figure(1)
py.plot(t,log_analysis(t,popt1[0],popt1[1]),color='blue')
py.plot(t,log_analysis(t,-np.log(2)/153,popt1[1]),color='green')
py.errorbar(t,np.log(N_s),color='green',yerr=error/(dt*N_s),ecolor='red')
hl1=-np.log(2)/popt1[0]
popt2,pcov2 = curve_fit(non_linear,t,N_s,p0=[-1,N_s[0]])
print(popt2)
py.figure(2)
py.plot(t,non_linear(t,popt2[0],popt2[1]),color='blue')
py.plot(t,non_linear(t,-1/153,popt2[1]),color='green')
hl2=-1/popt2[0]
py.errorbar(t,N_s,color='green',yerr=error/dt,ecolor='red')


