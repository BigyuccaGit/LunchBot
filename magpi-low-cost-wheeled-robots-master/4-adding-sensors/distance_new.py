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

# Set up main operations

def backwards():
  robot.backward()
  sleep(1.0)
  robot.stop()    
  
def right_spin():
  print("RIGHT SPIN")
  robot.left_motor.forward()
  robot.right_motor.backward()
  sleep(1.0)
  robot.stop()
  
def left_spin():
  print("LEFT SPIN")
  robot.right_motor.forward()
  robot.left_motor.backward()
  sleep(1.0)
  robot.stop()
  
coin_toss=[left_spin, right_spin]
def random_spin():
  coin_toss[random.randint(0,1)]()

spin_options=[random_spin, right_spin, left_spin, random_spin]
#              failsafe,   left sensor, right sensor, both sensors
def choose_spin(r_in_range, l_in_range):
  option = (r_in_range << 1) + l_in_range
  #spin_option[option]()
  print(r_in_range, l_in_range, option)
  return spin_options[option]
  
# Ensure it will stop
atexit.register(robot.stop)

# Start main Loop forever
while True:

  # Sent robot forward
  print("FORWARD")
  robot.forward()
  print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)

  # Wait for object to come in range
  while not r_sensor.in_range and not l_sensor.in_range: 
  #  print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)
    sleep(0.01) 

  # Stio the robot
  robot.stop()
  print("STOP")

  # Choose which spin option to do in a moment based on current settings
  spin_option=choose_spin(r_sensor.in_range, l_sensor.in_range)

  # Go Backwards
  print("BACKWARD")
  backwards()  

  # Execute chosen spin option
  print("SPIN")
  spin_option()
  
