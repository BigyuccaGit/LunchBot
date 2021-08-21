import gpiozero
import time
import sys

speed=float(sys.argv[1])

print("Speed is ", speed)

motorr = gpiozero.Motor(forward=27, backward=17)
motorl = gpiozero.Motor(forward=24, backward=23)

try:
    # Robot actions here
    motorr.forward(speed)
    time.sleep(5)
    motorr.stop()

    motorl.forward(speed)
    time.sleep(5)
    motorl.stop()

    motorr.backward(speed)
    time.sleep(5)
    motorr.stop()

    motorl.backward(speed)
    time.sleep(5)
    motorl.stop()

finally:
    motorr.stop()
    motorl.stop()
