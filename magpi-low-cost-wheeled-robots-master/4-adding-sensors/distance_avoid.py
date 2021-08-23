from signal import pause
import atexit
import gpiozero
import time
from gpiozero.tools import scaled, negated, booleanized
from gpiozero.pins.pigpio import PiGPIOFactory

# Parameters
speed = 1.0
threshold_distance_cm=20 #cm
queue_len=3
hysteresis_cm=2

threshold_distance=threshold_distance_cm/100.0
hysteresis=hysteresis_cm/100.0


factory = PiGPIOFactory()

# Instantiate robot
robot = gpiozero.Robot(right=(27, 17), left=(24, 23))

#robot.right_motor.forward()
#time.sleep(5.0)
#robot.right_motor.stop()

#robot.left_motor.forward() 
#time.sleep(5.0) 
#robot.left_motor.stop() 
 
#if 1==1:
#  pause()

# Instantiate sensors
right_distance_sensor  = gpiozero.DistanceSensor(echo=5,  trigger=6,  max_distance=1, threshold_distance=threshold_distance, queue_len=queue_len, pin_factory=factory)
left_distance_sensor = gpiozero.DistanceSensor(echo=13, trigger=26, max_distance=1, threshold_distance=threshold_distance, queue_len=queue_len, pin_factory=factory)

# Ensure it will stop
atexit.register(robot.stop)

# Source/value setup so opposite motor reverses when object detected, thus robot turns away
robot.right_motor.source = scaled(booleanized(left_distance_sensor,threshold_distance,1), -speed, speed)
robot.left_motor.source = scaled(booleanized(right_distance_sensor,threshold_distance,1), -speed, speed)

# Wait for something to happen
pause()
