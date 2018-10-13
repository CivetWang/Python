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
d = 7.5/100
D = 32.2/100
d1 = 5/100
R=(D-d)/2
n=130
mu_0=4*np.pi-10**-7
k = (4/5)**(3/2)*mu_0*n/(R*2**(1/2))

#BcS = []
#Bc_error = []
#for i in range(len(V)):
#    Bc = (4/5)**(3/2)*(4*np.pi*10**-7)*n*I[i]/R
#    BcS.append(Be)
#    Bc_error.append(Bc*np.sqrt((0.0005/R)**2+(0.0005/I[i])**2))
    
#BcS = np.array(BcS)
#Bc_error = np.array(Bc_error)

def f(x,a,b):
    return a*x+b

popt,pcov=curve_fit(f,I,V**(1/2)/r)
em=popt/k
em=em**2
me=pcov/k
print(em[0],'+-',me[0,0])



