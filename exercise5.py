# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pylab as pl
from scipy.optimize import curve_fit
import  matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import histogram
from scipy.special import gamma as Gamma

def g(x,a,b):
    return b*2**(a*x)

t,num = np.loadtxt('Radioctive Activity-Fiesta Plate(3sec. Dwell).txt',unpack=True)
bg = np.loadtxt('Background20min.txt')

bgn = np.average(bg)*3/10 #average background noise per counting interval
num -= bgn

def pdf(a,mu):
    sigma = np.sqrt(mu)
    return mlab.normpdf(a,mu,sigma)

def pmf(n,mu):
    return np.exp(-mu)*(mu**n)/Gamma(n+1)
b =10
#pre abalysis
initial_guess = [-1,num[0]]
popt1,pcov1 = curve_fit(g,t*3,num,p0=initial_guess)
thalf2 = -1/popt1[0]
print(thalf2)
pl.figure(1)
plt.plot(t*3,g(t*3,popt1[0],popt1[1])-num,'b.')
pl.figure(2)
hist,bin_edges = histogram(num,bins=b)

bin_edges = np.delete(bin_edges,b)
count = bin_edges+(bin_edges[1]-bin_edges[0])/2
initial_guess1 = [70]
popt,pcov = curve_fit(pdf,count,hist/sum(hist),p0=initial_guess1)
popt1,pcov1 = curve_fit(pmf,count,hist/sum(hist),p0=initial_guess1)
plt.hist(num,bins=b)
plt.plot(count,np.sum(hist)*pdf(count,popt[0]))
plt.plot(count,np.sum(hist)*pmf(count,popt1[0]),'r.')
#plt.plot(count,hist/sum(hist),'b.')