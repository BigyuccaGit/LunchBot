from signal import pause
import atexit
import gpiozero
from gpiozero.tools import scaled, negated

speed = 0.5

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))
 
left_obstacle_sensor = gpiozero.DistanceSensor(echo=5, trigger=6, max_distance=1, threshold_distance=0.2)
right_obstacle_sensor = gpiozero.DistanceSensor(echo=13, trigger=26, max_distance=1, threshold_distance=0.2)

# Ensure it will stop
atexit.register(robot.stop)

robot.right_motor.source = scaled(left_obstacle_sensor, -speed, speed)
robot.left_motor.source = scaled(right_obstacle_sensor, -speed, speed)

pause()
