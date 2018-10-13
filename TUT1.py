# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:14:36 2017

@author: Civet
"""
#a better use for the while loop
from numpy.random import randint # choose a random integer 
sumdice=0
counter=0
while sumdice!=12:
    #roll a pair of dice until they're faces add to 12 (two sixes!)
    #randint is quirky, and needs the maximum value to be 1 higher
    dice = [randint(1,7),randint(1,7)]
    sumdice=dice[0]+dice[1]
    counter+=1
print("%d rolls"%counter) #should be ~36, but it's random and can finish at any time