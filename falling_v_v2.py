from math import *
from pylab import *
from numpy import *

# define some constant parameters

g = 9.8
m = 1.0
b = 2.0   # linear drag parameter

a = b**2/(m*g)  # quadratic drag parameter cooked to give the same termional velocity as linear

#  First calculate the linear drag result from the analytic formula

#time  step in seconds
dt = 0.01

t = arange(0.0,4.0,dt)       # an array of times to plot up to 4 seconds
v1 = (m*g/b)*(1.0-exp(-b*t/m))      # makes an array of velocities for v1 = linear drag

n = len(t)    # the number of data points.  Arrays go from 0 to n-1.

#  Now solve the quadratic drag case by time stepping

v2 = zeros(n) # empty array to hold v2 = quadratic drag velocity values

v2[0] = 0.0  # initial condition

for i in range(1,n):                          # range function omits last index at npts
    v2[i] = v2[i-1] + (g-(a/m)*(v2[i-1])**2)*dt  # time step formula for quadratic drag

#  make a comparison plot

terminal_v = m*g/b*ones(n)        # a constant array of the terminal velocity
free_fall_v = g*t                   # an array to show the no drag free fall case

plot(t,v1,"r--", t,v2,"g",  t,free_fall_v,"b", t,terminal_v,"c")

ylim([0.0,6.0])                         # just to make the plot look nice
title("Falling with drag linear and quadratic in v")
xlabel("time")
ylabel("position")
legend(("linear drag","quadratic drag","free fall","terminal velocity"),loc="lower right")

show()


