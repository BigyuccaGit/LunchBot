from robot import Robot
from robot_imu import RobotImu
from delta_timer import DeltaTimer
from time import sleep

robot=Robot()
imu=RobotImu()
delta=DeltaTimer()

angle=90
yaw=0.0
speed = 100
while yaw < angle:
    sleep(0.001)
    dt,elapsed = delta.update()
    gyro=imu.read_gyroscope()
    yaw += gyro.z * dt

    if angle - yaw > 30:
        speed = 100
    else:
        speed = 60
    #speed = 70 #max(0,(angle-yaw)/angle *100)
    robot.speeds(-speed, speed)

print("Yaw = ", yaw)
robot.stop()

