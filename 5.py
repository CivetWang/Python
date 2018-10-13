# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:09:27 2017

@author: Civet
"""
import pylab
pylab.figure(figsize=(8,2)) #different figsize
x=pylab.arange(0,8*pylab.pi,0.05*pylab.pi)
y=pylab.sin(x)
pylab.plot(x,pylab.sin(x),color='red',label='sine', linewidth=5) # a thick line
pylab.plot(x,y**2,color='green',label='cosine',linestyle='--') # a dashed line
pylab.legend(loc='lower right')
pylab.xlabel("x axis label") # add a label to the x axis
pylab.ylabel('y axis label')
pylab.title("Plot title");