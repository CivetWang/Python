# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pylab as pl
from scipy.optimize import curve_fit
import  matplotlib.pyplot as plt

i,v = np.loadtxt('cell.txt',unpack=True)

di,dv = np.loadtxt('cell error.txt',unpack=True)
dv1=np.loadtxt('error1.txt',unpack=True)
dv2=np.loadtxt('error2.txt',unpack=True)
dv3=np.loadtxt('error3.txt',unpack=True)
dv4=np.loadtxt('error4.txt',unpack=True)
i1,v1 = np.loadtxt('regular.txt',unpack=True)
i2,v2 = np.loadtxt('regular - 10V.txt',unpack=True)
i3,v3 = np.loadtxt('regular - 15V.txt',unpack=True)
i4,v4 = np.loadtxt('regular - 20V.txt',unpack=True)
i /=1000
i1 /=1000
i2 /=1000
i3 /=1000
i4 /=1000
plt.figure(1)
plt.plot(i,v)
plt.figure(2)
plt.plot(i1,v1)
plt.figure(3)
plt.plot(i2,v2)
plt.figure(4)
plt.plot(i3,v3)
plt.figure(5)
plt.plot(i4,v4)
def power_supply(i,v0,R):
    return v0-R*i

popt,pcov = curve_fit(power_supply,i,v,sigma=dv)
popt1,pcov1 = curve_fit(power_supply,i1,v1,sigma=dv1)
popt2,pcov2 = curve_fit(power_supply,i2,v2,sigma=dv2)
popt3,pcov3 = curve_fit(power_supply,i3,v3,sigma=dv3)
popt4,pcov4 = curve_fit(power_supply,i4,v4,sigma=dv4)
print(popt[0],'+-',pcov[0,0],'    ',popt[1],'+-',pcov[1,1])
print(popt1[0],'+-',pcov1[0,0],'    ',popt1[1],'+-',pcov1[1,1])
print(popt2[0],'+-',pcov2[0,0],'    ',popt2[1],'+-',pcov2[1,1])
print(popt3[0],'+-',pcov3[0,0],'    ',popt3[1],'+-',pcov3[1,1])
print(popt4[0],'+-',pcov4[0,0],'    ',popt4[1],'+-',pcov4[1,1])