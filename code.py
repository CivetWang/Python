# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:52:17 2017

@author: hengl
"""

import numpy as np
import pylab as pl
from scipy.optimize import curve_fit
import  matplotlib.pyplot as plt

g1 = np.loadtxt('g1.txt')
g2 = np.loadtxt('g2.txt')
dg = 0.1 * 0.10055 / 10**5
g1 /= 10**5
g2 /= 10**5
dR = 3.95
g = 9.804253
G = 6.67*10**-11
mf = 10**6
Msun = 2.0*10**30
Rsun = 1.5*10**11
Mmoon = 7.4*10**22
Rmoon = 4.0*10**8
gs = G*mf/(dR**2)

def chi(x0,x,dx,nu):
    return sum(((x0-x)/dx)**2)/nu

'''
R1 = -2*dR*g/(np.average(g1)+gs/100)
R2 = -2*dR*g/(np.average(g2))
print(R1)
print(R2)
'''
floor = np.arange(3,14)
nu = len(floor)-2
tempfloor = np.zeros(len(floor))
for i in range(len(floor)):
    tempfloor[i]=sum(1/np.arange(1,floor[i])**2)-sum(1/np.arange(1,16-floor[i])**2)

def gravity(floor,R,g0):
    return g0+g*R**2/(R+floor*dR)**2-np.sin(moon_degree)*G*Mmoon/(Rmoon-R-floor*dR)**2-np.sin(sun_degree)*G*Msun/(Rsun-R-floor*dR)**2+G*mf/dR**2*tempfloor

initial_guess=[6400000,-9.0]
sun_degree = 33.15/180*np.pi
moon_degree = -21.44/180*np.pi
popt,pcov = curve_fit(gravity,floor,g1,p0=initial_guess)
print(popt[0])
print('the chi square is ',chi(g1,gravity(floor,popt[0],popt[1]),dg,nu))
plt.figure(1)
plt.plot(floor,gravity(floor,popt[0],popt[1]))
plt.plot(floor,g1)
sun_degree = 25.99/180*np.pi
moon_degree = -13.29/180*np.pi
popt1,pcov1 = curve_fit(gravity,floor,g2,p0=initial_guess)
print(popt1[0])
print('the chi square is ',chi(g2,gravity(floor,popt1[0],popt1[1]),dg,nu))
plt.figure(2)
plt.plot(floor,gravity(floor,popt1[0],popt1[1]))
plt.plot(floor,g2)



