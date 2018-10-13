# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:59:03 2017

Who is this author? Why isn't this your name here?
@author: Civet
"""
'''
Final grade 77/100
'''
#Q1
'''
10/10
'''
#Given settings
import numpy
h=.1
y=numpy.sin(numpy.arange(10)*h)
#create an output array
result=[]
#fill the array with results
for i in range(len(y)-1):
    result.append((y[i+1]-y[i])/h)
#output
print("Q1",result)  

#Q2
'''
10/10
'''
#Given settings
import numpy
h=.1
y=numpy.sin(numpy.arange(10)*h)
#SLice the y array
slice_one=y[0:8]
slice_two=y[1:9]
#compute the result
res=(slice_two-slice_one)/h
print("Q2",res)

#Q3
'''
Wrong tensiona and uncertainty
for the uncertainty calculation, do not hard-code the numnbers in. Work exclusively in variables
7/14
'''
#draw setting
import numpy
mass=105.2
vel=32.0
rad=70
g=9.8
#calculate Tension
#should be squared instead of numpy sqrt
T=mass*(numpy.sqrt(g**2+numpy.sqrt(vel**2/rad)))
# uncertainty
unc=numpy.sqrt((((numpy.sqrt((2*0.5*32)**2+(0.1/70)**2))*((vel**2/rad)**2))**(
        -1/2)*(1/2))/(numpy.sqrt(g**2+(vel**2/rad)**2))+(0.1**2/mass)**2)
print("Q3",T,"+-",unc,"N")

#Q4
'''
10/10
'''
import numpy
#load data
c=numpy.loadtxt('../sample-correlation.txt')
print("Q4",numpy.corrcoef(c,rowvar=False))

#Q5 imcomplete
'''
Missed the other mistake where linspace should use N+1 or b-dx
8/16
'''
import numpy as np
a, b = 0, np.pi /2
N = 20 # Number of intervals
dx = (b-a )/20#fixed order
x = np. linspace (a, b, N)
f = np.cos(x)
riemann_sum = np. sum(f * dx)
print ("Q5",riemann_sum )

#Q6
'''
12/12 it would be better to do the calculation vectorized using np.sum without the loop
'''
def average(x):
    res=0
    for i in range(len(x)):
        res=res+x[i]#sum
    res=(res/len(x))#average
    print ("Q6",res)

#Q7
'''
the funciton should returnt he mean and the std. dev according to the question. Also you should divide by the len(x) -1 not the mean of x squared. 
8/14
'''
import numpy
def stdev(x):
    mean_x=x.sum()/(len(x))
    #mean
    stv=numpy.sqrt((x**2).sum()/(len(x))-mean_x**2)
    #standard deviation
    print("Q7","mean_x is",mean_x,",","stdev_x is",stv)
    #output
    
#Q8
'''
correct final answer, but no units included
12/14
'''
import numpy
#load data
V=numpy.loadtxt('../sample-correlation.txt',usecols=0)
I=numpy.loadtxt('../sample-correlation.txt',usecols=1)
#set variables
V_mean=numpy.average(V)
I_mean=numpy.average(I)
#calculate parameters
b_hat=numpy.sum((V-V_mean)*(I-I_mean))/numpy.sum((I-I_mean)**2)
a_hat=V_mean-b_hat*I_mean
print("Q8","Resistance is",b_hat,"Voltage offset is",a_hat)
