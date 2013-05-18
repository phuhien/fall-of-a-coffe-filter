from __future__ import division
from numpy import *
from matplotlib.pyplot import *
import math

g = 9.81 #gravity
v = -0.5 #terminal velocity
 
# Finite Difference
# input:
# positionArray: array of positions
# timeArray: array of times
# output:
# the velocity and acceleration at the position
# Time in seconds: data[0,:]
# y-axis position in meters: data[1,:]

#emperical data given in report
data = array([[.2055,.2302,.2550,.2797,.3045,.3292,.3539,.3786,.4033,.4280,
				.4526,.4773,.5020,.5266,.5513,.5759,.6005,.6252,.6498,.6744,
				.6990,.7236,.7482,.7728,.7974,.8220,.8466],
				[.4188,.4164,.4128,.4082,.4026,.3958,.3878,.3802,.3708,.3609,
				.3505,.3400,.3297,.3181,.3051,.2913,.2788,.2667,.2497,.2337,
				.2175,.2008,.1846,.1696,.1566,.1393,.1263]])
timeArray = data[0, :]
positionArray = data[1, :]
vel = []
acc = []


def calculateVelocity(positionArray, timeArray):
    vel = (positionArray[2:] - positionArray[:-2])/(timeArray[2:] - timeArray[:-2])
    return vel
 
def calculateAcceleration(positionArray, timeArray):
    acc = (positionArray[2:] - 2*positionArray[1:-1] + positionArray[:-2])/(0.5*(timeArray[2:] - timeArray[:-2]))**2
    return acc

vel = calculateVelocity(positionArray, timeArray)
acc = calculateAcceleration(positionArray, timeArray)
 
subplot(221)
plot(timeArray, positionArray, 'y^-')
xlabel('Time (s)')
ylabel('Position (m)')
title('Position Vs. Time')
subplot(222)
plot(timeArray[1:-1], vel, 'go-')
xlabel('Time (s)')
ylabel('Velocity (m/s)')
title('Velocity Vs. Time')
subplot(223)
plot(timeArray[1:-1], acc,'bs')
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
title('Acceleration Vs. Time')
subplot(224)
plot(vel, acc,'ro')
xlabel('Velocity (m/s)')
ylabel('Acceleration (m/s^2)')
title('Velocity Vs. Acceleration')
show()

# Runge Kutta Method
# input: 
#	fn:		function
#	t:		time variable (at step n)
#	dPos:	position variable (at step n)
#	tStep:	time step
# output:
#	the next position based on the current position
def RungeKutta(fn, dPos, tStep):
	k1 = fn(dPos)*tStep
	k2 = fn(dPos + (k1/2))*tStep
	k3 = fn(dPos + (k2/2))*tStep
	k4 = fn(dPos + k3)*tStep
	return dPos + (1/6)*(k1 + 2*k2 + 2*k3 + k4)

y=array(data[1])
t=array(data[0]) 
dt_y=t[1:]-t[0:-1] 
velocity=(y[1:]-y[0:-1])/dt_y  

# Falling body approximate solution (linear)
# input:
#	rgState:	a vector including the position and velocity of the body at some point in time
# output:
#	an array containting the derivative evaluated at that point
def linearFallingModel(rgState):
	return array([rgState[1], -g*(1 - rgState[1]/v)])
	
# Falling body approximate solution (quadratic)
# input:
#	rgState:	a vector including the position and velocity of the body at some point in time
# output:
#	an array containting the derivative evaluated at that point
def quadraticFallingModel(rgState):
	return array([rgState[1], -g*(1 - (rgState[1]/v)**2)])
	
def quadraticFallingModelVel(rgState):
        return array([rgState[1], -g*(1 - (rgState[1]/v)**2)])
 
# Approximate solutions 
v0=velocity[0]
linearModel = [array([positionArray[0], v0])]		# assuming no intial velocity, may change to assume 
quadraticModel = [array([positionArray[0], v0])]		# initial velocity found via finite difference
 
for it in timeArray[0:-1]:
	linearModel.append(RungeKutta(linearFallingModel, linearModel[-1], timeArray[it+1] - timeArray[it]))
	quadraticModel.append(RungeKutta(quadraticFallingModel, quadraticModel[-1], timeArray[it+1] - timeArray[it]))

linear_velocity=zip(*linearModel)[1]  
quadratic_velocity=zip(*quadraticModel)[1]
linear_position = zip(*linearModel)[0]  
quadratic_position = zip(*quadraticModel)[0]


figure(2)
subplot(221)
plot(timeArray, linear_position, 'r^-', label = 'Linear Simulation')
plot(timeArray, quadratic_position, 'bo-', label = 'Quadratic Simulation')
plot(timeArray, positionArray, 'y^-', label = 'Observed Data')
title('Simulated and Empirical Positions')
xlabel('Time (s)')
ylabel('Position (m)')
legend() 
subplot(222)
plot(timeArray[1:-1], vel, 'go-', label = 'empirical data')
plot(timeArray, linear_velocity, 'r-', label = 'Linear Simulation')
plot(timeArray, quadratic_velocity, 'b-', label = 'Quadratic Simulation')
xlabel('Time (s)')
ylabel('Velocity (m/s)')
title('Velocity Vs. Time')
legend()
show()
