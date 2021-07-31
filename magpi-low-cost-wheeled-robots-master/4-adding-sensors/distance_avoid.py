from signal import pause
import atexit
import gpiozero
from gpiozero.tools import scaled, negated, booleanized

# Parameters
speed = 0.5
threshold_distance=0.2 #meters

# Instantiate robot
robot = gpiozero.Robot(left=(27, 17), right=(24, 23))
 
# Instantiate sensors
left_distance_sensor = gpiozero.DistanceSensor(echo=5, trigger=6, max_distance=1, threshold_distance=0.2)
right_distance_sensor = gpiozero.DistanceSensor(echo=13, trigger=26, max_distance=1, threshold_distance=0.2)

# Ensure it will stop
atexit.register(robot.stop)

# Source/value setup so opposite motor reverses when object detected, thus robot turns away
robot.right_motor.source = scaled(negated(booleanized(left_distance_sensor,0,threshold_distance)), -speed, speed)
robot.left_motor.source = scaled(negated(booleanized(right_distance_sensor,0,threshold_distance)), -speed, speed)

# Wait for something to happen
pause()
