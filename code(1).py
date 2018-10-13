# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


x1,y1 = np.loadtxt('track9.txt',unpack=True)

def pdf_2D(r,Dt):
    return r/(2*Dt)*np.exp(-r**2/(4*Dt))

bins = 30
dx = x1[:-1]-x1[1:]
dy = y1[:-1]-y1[1:]
r = np.sqrt(dx**2+dy**2)
y,binEdges = np.histogram(r,bins=bins)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
menStd = np.sqrt(y)
weights = [1/max(_,0.001) for _ in menStd]
width = 5/bins
popt,pcov = curve_fit(pdf_2D,bincenters,y,sigma=weights)
plt.figure(1)
#plt.plot(y1,x1)
plt.plot(np.arange(1,120),r)
plt.figure(2)
plt.bar(bincenters,y,width=width,yerr=menStd,ecolor='yellow')
Dt=sum(r**2)/(4*len(r))
plt.plot(bincenters,np.sum(y)*pdf_2D(bincenters,Dt))
plt.figure(3)
plt.plot(bincenters,y/np.sum(y))
