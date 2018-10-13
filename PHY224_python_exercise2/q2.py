# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:18:55 2017

@author: student
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

volt, current = np.loadtxt('unknown.txt',unpack=True)

def ohm(x,a):
    return a*x

def chi(x0,x,dx,nu):
    return sum(((x0-x)/dx)**2)/nu

n=1
N=10
nu = N-n

dcurrent = 0.002 * current
p_opt , p_cov = curve_fit(ohm , volt , current )



y = p_opt[0]*volt
dy = y-current

print('the slope is', p_opt[0])
print('the resistance is',1/p_opt[0])
#pl.plot(x,y,linewidth=3)
plt.figure(1)
plt.plot(volt,current,'rs')
plt.plot(volt,y,'y+')
plt.figure(2)
plt.plot(volt,dy,'bo')
print('chi-suqared =',chi(current,y,dcurrent,nu))