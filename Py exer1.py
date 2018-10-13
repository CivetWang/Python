# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:34:20 2017

@author: Civet
"""
import pylab
k=11.451
m=0.2013
omega_constant=pylab.sqrt(k/m)

dt=0.01
t=pylab.arange(0,10.00,dt)
y=pylab.zeros(len(t))
v=pylab.zeros(len(t))

y[0]=24.086
v[0]=0.21371

for i in range(len(t)-1):
    y[i+1]=y[i]+dt*v[i]
    v[i+1]=v[i]-dt*y[i+1]*k/m

pylab.figure(0)
pylab.plot(t,y)
pylab.xlabel("Time(s)") 
pylab.ylabel("Position(m)")
pylab.title("Position Vs. Time")
pylab.savefig("Position Vs. Time.png")

pylab.figure(1)
pylab.plot(t,v)
pylab.xlabel("Time(s)") 
pylab.ylabel("Velocity(m/s)")
pylab.title("Velocity Vs. Time")
pylab.savefig("Velocity Vs. Time.png")

pylab.figure(2)
pylab.plot(y,v,linewidth=0.1)
pylab.xlabel("Position(m)") 
pylab.ylabel("Velocity(m/s)")
pylab.title("Velocity Vs. Position")
pylab.savefig("Velocity Vs. Position.png")

E=0.5*m*(v**2)+0.5*k*y**2
pylab.figure(3)
pylab.plot(t,E)
pylab.xlabel("Time(s)") 
pylab.ylabel("Energy")
pylab.title("Energy Vs. Time")
pylab.savefig("Energy Vs. Time.png")