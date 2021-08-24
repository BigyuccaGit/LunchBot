from signal import pause
import atexit
import gpiozero
import time
from gpiozero.tools import scaled, negated, booleanized
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import random

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

# Instantiate sensors
r_sensor  = gpiozero.DistanceSensor(echo=5,  trigger=6,  max_distance=1, threshold_distance=threshold_distance, queue_len=queue_len, pin_factory=factory)
l_sensor = gpiozero.DistanceSensor(echo=13, trigger=26, max_distance=1, threshold_distance=threshold_distance, queue_len=queue_len, pin_factory=factory)

# Ensure it will stop
atexit.register(robot.stop)

# Source/value setup so opposite motor reverses when object detected, thus robot turns away
#robot.right_motor.source = scaled(booleanized(left_distance_sensor,threshold_distance,1), -speed, speed)
#robot.left_motor.source = scaled(booleanized(right_distance_sensor,threshold_distance,1), -speed, speed)

# Wait for something to happen
#pause()

while True:
  print("FORWARD")
  robot.forward()
  print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)

  while not r_sensor.in_range and not l_sensor.in_range: 
  
  #  print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)
    sleep(0.01) 
  
  print("STOP")
  robot.stop()

  print("BACKWARD")
  robot.backward()
  sleep(1.0)
  robot.stop()  

  print("SPIN")
  coin=random.randint(0,1)
  if coin == 0: 
    robot.left_motor.forward()
    robot.right_motor.backward()
  else:
    robot.right_motor.forward()
    robot.left_motor.backward()
  sleep(1.0)
  robot.stop()
