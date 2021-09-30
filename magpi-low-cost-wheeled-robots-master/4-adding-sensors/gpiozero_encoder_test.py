from gpiozero import RotaryEncoder, Motor
from time import sleep
import atexit
from gpiozero import DigitalInputDevice
import time
import logging

logger = logging.getLogger("test_encoders")

#class EncoderCounter(object):
#    def __init__(self, pin_number):
#        self.pulse_count = 0
#        self.device = DigitalInputDevice(pin=pin_number)
#        self.device.pin.when_changed = self.when_changed
#        self.direction = 1
#        
#    def when_changed(self, time_ticks, state):
#        self.pulse_count += self.direction
#
#    def set_direction(self, direction):
#        self.direction = direction


#rotor = RotaryEncoder(a=8, b=7, wrap=True)

motorr = Motor(forward=27, backward=17)
#motorl = Motor(forward=23, backward=24)

speed = 1

motorr.forward(speed)
#motorl.forward(speed)

bounce=0.1

sleep(0.1)
rotor = RotaryEncoder(a=7, b=8, wrap=False, max_steps=0, bounce_time = bounce*0.0001)

#rotorr = EncoderCounter(7)
#rotorl = EncoderCounter(8)

atexit.register(motorr.stop)

sample=0
last=0
forward=0
backward=0
stopped=0
while (sample <= 10):

#    print("Steps = ", rotor.steps, rotor.value, sample)
    thisr = rotor.steps
    #thisl = rotorl.pulse_count
#    if abs(last - thisr) <= 5:
#      status="Stopped"
#      stopped += 1
#    elif last < thisr:
#      status="Forward"
#      forward += 1
#    else:
#      status="Backward"
#      backward += 1

    print("Steps = ", thisr, thisr-last, sample)
    sample = sample+1
    sleep(0.1)

 #   if stopped > 0 :
 #       motorr.stop()
        #motorl.stop()

#    if sample == 50:
#        motorr.backward(speed)
#        motorl.backward(speed)
#        rotorr.direction = -1
#        rotorl.direction = -1

#    if sample == 100:
#        motorr.stop()
#        #motorl.stop()

    last=thisr
        
#pause()

motorr.stop()

print("Summary", forward, backward, stopped)


