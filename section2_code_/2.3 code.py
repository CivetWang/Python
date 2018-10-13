# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 17:20:04 2017

@author: student
"""
import pylab

dt = 0.001

omega = 8.727

gamma = 0.0311
m = 0.218
k = 16.6

t = pylab.arange(0,120.0,dt)
y = pylab.zeros(len(t))
v = pylab.zeros(len(t))

y[0] = 6.83
v[0] = 0
for i in range(len(t)-1):
    y[i+1] = y[i] + dt * v[i]
    v[i+1] = v[i] - dt * (y[i+1] * (omega**2) + gamma * v[i])
    
pylab.figure(1)
pylab.plot(t,y,linewidth = 1)

E = 0.5 * m * v**2 + 0.5 * k * y**2

pylab.figure(2)
pylab.plot(t,E,linewidth = 1)