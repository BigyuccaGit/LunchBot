import gpiozero
import time

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))

try:
    # Robot actions here
    robot.backward()
    time.sleep(10)
finally:
    robot.stop()
