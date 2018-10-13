# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:21:31 2017

@author: Civet
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

I,V = np.loadtxt('electron.txt',unpack=True)

r = 3.5/100
dr=0.001
d = 7.5/100
D = 32.2/100
d1 = 5/100
R=D-d
n=130
mu_0=4*np.pi*10**-7
k = (4/5)**(3/2)*mu_0*n/(R*2**(1/2))
r *= D/d1
dr *= D/d1

def f(x,a,b):
    return a*(x-b)

popt,pcov=curve_fit(f,I,np.sqrt(V))
em=popt[0]/(k*r)
em=em**2
me=2*np.sqrt(em)*np.sqrt(pcov[0][0]+dr**2)/(k*r)
print(em,'+-',me)

plt.figure(1)
plt.plot(I,np.sqrt(V),'.')
plt.plot(I,f(I,popt[0],popt[1]))

