import gpiozero
import time
import sys

speed=float(sys.argv[1])

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))

try:
    # Robot actions here
    robot.forward(speed)
    time.sleep(10)
finally:
    robot.stop()
