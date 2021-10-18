from gpiozero import Motor
from time import sleep
import atexit
#from gpiozero import DigitalInputDevice

from encoder_counter import EncoderCounter
import time
import logging

def exit_all():
  motorr.stop()
  motorl.stop()
     

logger = logging.getLogger("test_encoders")

motorl = Motor(forward=24, backward=23)
motorr = Motor(forward=27, backward=17)

rotorl = EncoderCounter(8,'L')
rotorr = EncoderCounter(7,'R')

print(rotorl.device.pin.edges, rotorr.device.pin.edges )

#quit()

speed = 1
atexit.register(exit_all)

motorr.forward(speed)
motorl.forward(speed)

sleep(0.1)

sample=0

start_time=time.time()
stop_at_time=start_time+20

while time.time() < stop_at_time:
#     print(time.time(), rotorl.pulse_count, rotorl.pulse_last, rotorl.pulse_delta, rotorr.pulse_count, rotorr.pulse_last, rotorr.pulse_delta)
#     print(time.time(), rotorr.pulse_count, rotorr.pulse_delta)
     print(time.time(), rotorl.pulse_delta, rotorr.pulse_delta)
     sleep(0.1)


motorr.stop()
motorl.stop()
