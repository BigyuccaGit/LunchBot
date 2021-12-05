from robot import Robot
from robot_imu import RobotImu
from delta_timer import DeltaTimer
from time import sleep

robot=Robot(encoder=False, distance = False)
imu=RobotImu()
delta=DeltaTimer()

try:
    angle=90+45
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
            speed = 50
    
        robot.speeds(-speed, speed)
            
except KeyboardInterrupt:
    robot.stop()
    
finally:
    robot.stop()

