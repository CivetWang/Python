# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:27:22 2017

@author: Civet
"""

import numpy as np
from scipy.optimize import curve_fit
import  matplotlib.pyplot as plt
from matplotlib import mlab
from numpy import histogram 

sn,n=np.loadtxt('Radioctive Activity-Fiesta Plate(3sec. Dwell).txt',
                unpack=True)
B_g=np.loadtxt('Background20min.txt',unpack=True)
dtn=3
dtB_g=10


def g(x,a,b):
    return b*2**(a*x)

aB_g=np.average(B_g)/dtB_g*dtn
n=n-aB_g
mu=np.average(n)

def pdf(a, mu):
    sigma=np.sqrt(mu)
    return mlab.normpdf(a,mu,sigma)

pdf1=pdf(n,mu)

initial_guess = [-1,n[0]]
popt1,pcov1 = curve_fit(g,sn*3,n,p0=initial_guess)
print(popt1)
thalf2 = -1/popt1[0]
print(thalf2)
plt.figure(1)
plt.plot(sn*3,g(sn*3,popt1[0],popt1[1])-n,'r.')
plt.figure(2)
plt.plot(pdf1)

