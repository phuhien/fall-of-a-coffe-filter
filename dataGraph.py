from numpy import * 
from matplotlib.pyplot import * 
 
# Global Variables
dAccGrav = 9.81
dVelTerm = -0.5
 
# Finite Difference
# input:
#  positionArray:	array of positions
#	timeArray:	array of times
# output:
#	the velocity and acceleration at the position
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

