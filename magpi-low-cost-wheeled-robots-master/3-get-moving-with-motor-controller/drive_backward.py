import gpiozero
import time
import sys

if len(sys.argv) > 1:
    speed=min(float(sys.argv[1]),1)
else:
    speed=1
    
print("Speed is ", speed, "Argv length = ", len(sys.argv))

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))

try:
    # Robot actions here
    robot.backward(speed)
    time.sleep(10)
finally:
    robot.stop()
