# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:11:05 2017

@author: Civet
"""

import pylab # import pylab
source_file = "co2_annmean_mlo.txt"
comment_char="#"
year,co2 = pylab.loadtxt(source_file, 
                        usecols=(0,1),
                        unpack=True,
                        comments=comment_char)
pylab.plot(year,co2,'.',label="CO2 data")
pylab.xlabel("year")
pylab.ylabel("CO2 (ppm)")
pylab.title("Mauna Loa data")
pylab.legend(loc='lower right',numpoints=1);
#fit a straight line
def fitfunc(x,*p):
    return p[0]+p[1]*x
#import the fitting routine
from scipy.optimize import curve_fit
#call the fitting routine, remember to give initial values for the parameters
popt, pcov = curve_fit(fitfunc,year,co2,p0=[0,0])
#setup the figure
pylab.figure(figsize=(8,4))
#plot the data
pylab.plot(year,co2,'.',label="CO2 data")
#calculate the line fit by calling the fit function directly
fitted_data = fitfunc(year,*popt)
#plot the fitting line
pylab.plot(year,fitted_data,
            linewidth=2,
            label="linear".format(*popt))
#decorate the plot
pylab.xlabel("year")
pylab.ylabel("CO2 (ppm)")
pylab.title("Mauna Loa fit")
pylab.legend(loc='lower right',numpoints=1);
print("f(year) = a + b*year".format(*popt))
print("a = {0:9.3f} +- {1:6.3f} ppm".format(popt[0],pylab.sqrt(pcov[0,0])))
print("b = {0:9.3f} +- {1:6.3f} ppm/year".format(popt[1],pylab.sqrt(pcov[1,1])))
pylab.savefig("output_files/co2fit.pdf")
