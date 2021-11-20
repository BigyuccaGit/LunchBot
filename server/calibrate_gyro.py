from robot_imu import RobotImu
import time
import vpython as vp
import statistics as s

imu = RobotImu()

gyro_min = vp.vector(0, 0, 0)
gyro_max = vp.vector(0, 0, 0)

num=1000

xlist=num*[0]
ylist=num*[0]
zlist=num*[0]
for n in range(num):
    gyro = imu.read_gyroscope()
    gyro_min.x = min(gyro_min.x, gyro.x)
    gyro_min.y = min(gyro_min.y, gyro.y)
    gyro_min.z = min(gyro_min.z, gyro.z)

    gyro_max.x = max(gyro_max.x, gyro.x)
    gyro_max.y = max(gyro_max.y, gyro.y)
    gyro_max.z = max(gyro_max.z, gyro.z)

    offset = (gyro_min + gyro_max) / 2

    xlist[n]=gyro.x
    ylist[n]=gyro.y
    zlist[n]=gyro.z
    
    time.sleep(.01)

mean_value=vp.vector(s.mean(xlist), s.mean(ylist), s.mean(zlist))
median_value=vp.vector(s.median(xlist), s.median(ylist), s.median(zlist))

print(f"Zero offset: {offset}.")
print(f"Means: {mean_value}.")
print(f"Medians: {median_value}.")
