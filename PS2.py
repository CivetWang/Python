# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:09:00 2017

@author: Civet
"""

#Q1
#import numpy
#res=[]
#a=numpy.loadtxt('/to_combine/data_file_00.txt')
#b=numpy.loadtxt('/to_combine/data_file_01.txt')
#c=numpy.loadtxt('/to_combine/data_file_02.txt')
#res.append(a)
#res.append(b)
#res.append(c)
#print("Q1","Mean is ",numpy.mean(res),"standard deviation is ",numpy.std(res))

#Q2
import matplotlib.pyplot as py
import numpy
r=numpy.linspace(0.9,2.9,num=100)
rm=2**(1/6)
V= numpy.zeros(len(r))
for i in range(len(r)):
    V[i]=(rm/r[i])**12-2*((rm/r[i])**6)
py.figure(1)
py.plot(r,V)
py.xlabel("r") 
py.ylabel("V")
py.title("Lennard-Jones potential")
py.ylim(-1.5)
py.savefig("Lennard-Jones potential.pdf")

#Q3
import matplotlib.pyplot as py
import numpy
m=4.652*10**(-26)
ki=1.38*10**(-23)
V=numpy.linspace(0,1200,1200)
def Maxwell(v,T):
    part1=numpy.sqrt((m/(2*numpy.pi*ki*T))**3)
    part2=4*numpy.pi*(v**2)
    part3=(numpy.e)**((-m)*(v**2)/(2*ki*T))
    return part1*part2*part3
P1=[]
P2=[]
P3=[]
for i in range(len(V)):
    P1.append(Maxwell(V[i],80))
    P2.append(Maxwell(V[i],233))
    P3.append(Maxwell(V[i],298))
py.figure(2)
py.plot(V,P1,color='blue')
py.plot(V,P2,color='black')
py.plot(V,P3,color='red')
py.title("Maxwell-Boltzmann distribution for Nitrogen")
py.xlabel("Velocity(m/s)")
py.ylabel("Probility")
py.legend(['T=80K',"T=233K",'T=298K'],loc='upper right')
py.savefig('Maxwell-Boltzmann distribution for Nitrogen.pdf')

#Q4
res=[]
def one_plus_three(data):
    for i in range(len(data)):
        res.append(data[i][0]+data[i][2])
    print(res)
data = numpy.array (
        [[1 , 2 , 3 , 4] ,
         [4 , 3 , 2 , 1] ,
         [ -1 , 1 , -1 , 1] ,
         [0 , 0 , 1 , 0] ,
         [9 , 16 , 4 , 25]])
print(one_plus_three(data))

#Q5
import numpy as np
import matplotlib.pyplot as plt
V,T,E=np.loadtxt('sample_data.txt',unpack=True)
plt.figure(3)
plt.errorbar(V,T,yerr=E)
py.title("sample_data")
py.xlabel("Voltage")
py.ylabel("Temperature")
py.savefig('sample_data.pdf')
