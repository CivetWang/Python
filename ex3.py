# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pylab as pl
from scipy.optimize import curve_fit
import  matplotlib.pyplot as plt
dt=20

N,count = np.loadtxt('Cesium Radioactive Decay.txt',unpack=True)
N1,bg = np.loadtxt('Radioactive Background 20min(20secdwell).txt',unpack=True)

def f(x,a,b):
    return a*x+b

def g(x,a,b):
    return b*2**(a*x)

Ns = count-np.average(bg)
error = np.sqrt(count+np.average(bg))

Ns /= dt
error /= dt
t = N*20
'''
transformation method
'''
popt, pcov = curve_fit(f, t, np.log(Ns))
print(popt)
thalf1=-np.log(2)/popt[0]
print(thalf1)

'''
non-linear least-squares method
'''
initial_guess = [-1,Ns[0]]
popt1,pcov1 = curve_fit(g,t,Ns,p0=initial_guess)
print(popt1)
thalf2 = -1/popt1[0]
print(thalf2)


pl.figure(1)
pl.plot(t,g(t,popt1[0],popt1[1]),color='purple',label='best fit curve')
pl.plot(t,g(t,-1/153,popt1[1]),color='green',label='theoretical curve')
plt.errorbar(t,Ns,yerr=error,elinewidth=1,ecolor='red')
pl.legend(loc='upper right')
pl.xlabel('time(s)')
pl.ylabel('number of counts per second')

pl.figure(2)
pl.plot(t,f(t,popt[0],popt[1]),color='purple',label='best fit curve')
pl.plot(t,f(t,-np.log(2)/153,popt[1]),color='green',label='theoretical curve')
plt.errorbar(t,np.log(Ns),yerr=error/Ns,elinewidth=1,ecolor='red')
pl.xlabel('time(s)')
pl.ylabel('logarithm number of counts per second')
pl.legend(loc='upper right')

pl.figure(3)
pl.semilogy(t,g(t,popt1[0],popt1[1]),color='purple',label='best fit curve')
pl.semilogy(t,g(t,-1/153,popt1[1]),color='green',label='theoretical curve')
plt.errorbar(t,Ns,yerr=error,elinewidth=1,ecolor='red')
pl.legend(loc='upper right')
pl.xlabel('time(s)')
pl.ylabel('number of counts per second')

pl.figure(4)
pl.semilogy(t,f(t,popt[0],popt[1]),color='purple',label='best fit curve')
pl.semilogy(t,f(t,-np.log(2)/153,popt[1]),color='green',label='theoretical curve')
plt.errorbar(t,np.log(Ns),yerr=error/Ns,elinewidth=1,ecolor='red')
pl.xlabel('time(s)')
pl.ylabel('logarithm number of counts per second')
pl.legend(loc='upper right')