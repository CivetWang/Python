# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:27:42 2017

@author: student
"""

import pylab as pl
import numpy as np
t,y,dy = np.loadtxt('position data.txt', unpack = True)
t,v = np.loadtxt('velocity data.txt', unpack = True)

y /= 100
v /= 100
m = 0.218
k = 16.6
E = 0.5 * m * v**2 + 0.5 * k * y**2
pl.plot(t,E)


'''
def amp(x):
    y = np.zeros(len(x))
    for i in range(len(x)-100):
        if x[i] == np.max(x[i:i+100]):
            y[i] = x[i]
    return y
'''
