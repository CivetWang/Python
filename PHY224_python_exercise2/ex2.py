# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:57:19 2017

@author: student
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#import data from experinment and unpack to arrays
volt, current = np.loadtxt('unknown.txt',unpack=True)
#define the function as
def ohm(x,a,b):
    return a*x + b

def chi(x0,x,dx,nu):
    return sum(((x0-x)/dx)**2)/nu

dcurrent = 0.002 * current
p_opt , p_cov = curve_fit(ohm , volt , current , (1,0), dcurrent , True)



y = p_opt[0]*volt+p_opt[1]
dy = y-current

print('the slope is', p_opt[0])
print('the intercept is',p_opt[1])
print('the resistance is',1/p_opt[0])
#pl.plot(x,y,linewidth=3)
plt.figure(1)
plt.plot(volt,current,'rs')
plt.plot(volt,y,'y+')
plt.figure(2)
plt.plot(volt,dy,'bo')
print('chi-suqared =',chi(current,y,dcurrent,nu))