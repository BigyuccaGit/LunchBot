import gpiozero
import time
import sys
from pins import *

speed=1

#print("Speed is ", speed)

motorr = gpiozero.Motor(forward=R_MOTOR_F_PIN, backward=R_MOTOR_B_PIN)
motorl = gpiozero.Motor(forward=L_MOTOR_F_PIN, backward=L_MOTOR_B_PIN)

try:
    motorr.backward(speed)
    motorl.backward(speed)
    time.sleep(1)
except KeyboardInterrupt:
    motorr.stop()
    motorl.stop()
finally:
    motorr.stop()
    motorl.stop()
