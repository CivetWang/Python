from pylab import *
# Problem Set 1 Template  Plotting analytic solutions
#a(t), v(t) and x(t) for F=-mbexp(cv)

#constants for force
A = 0.2
B = 1.0

#initial conditions
x0= 0.0
v0= 5.0

#time step
dt = 0.01
t = arange(0.0,10.0,dt)      # an array of times to plot up to 10 seconds

# npts = len(t)  # number of time steps

#  analytic expressions
#acceleration
a = -B/(A*B*t+exp(v0*A))      # your expression here

#velocity
v = log(A*B*t+exp(-v0*A))/(-A)     # your expression here

#position
x = (A*B**2)*t-B(exp(-v0*A+A*B*t))*ln(-v0*A+A*B*t)+A*B*v0*exp(-v0*A)      # your expression here

# numerical solution via time stepping

# an = zeros(npts)    # zero arrays for holding the numerical solutions
# vn = zeros(npts)
# xn = zeros(npts)

# set up your recursion scheme for finding an, vn and xn here
#
#  your loops go here
#  note that you must figure out vn to calculate an
#

#set up first plotting window
subplot(3,1,1)
#plot a(time), label it, turn on the grid.
plot(t,a)
# plot(t,a, t, an)  # comparison plot for analytic and numerical results
ylabel('a(t)')
grid('on')

#set up next plotting window, plot v(time)
subplot(3,1,2)
plot(t, v)
# plot(t,v, t,vn)  # comparison plot for analytic and numerical results
ylabel('v(t)')
grid('on')

#and x(time); label y and x axis for bottom plot.
subplot(3,1,3)
plot(t, x)
# plot(t,x, t, xn)  # comparison plot for analytic and numerical results
ylabel('x(t)')
xlabel('t')
grid('on')

#super title (goes at top of window)
suptitle('Exponential force solutions')
#save a hardcopy of the figure
#savefig('q4_partb.pdf')
#show the plot on the screen
show()
