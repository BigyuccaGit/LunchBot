from gpiozero import Motor
from time import sleep
import atexit
from gpiozero import DigitalInputDevice
import time
import logging

logger = logging.getLogger("test_encoders")

class EncoderCounter(object):
    def __init__(self, pin_number):
        self.pulse_count = 0
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.when_changed = self.when_changed
        self.direction = 1
        self.last=0
        self.pulse_last=0
        self.record=False
        self.list=[]
 
    def when_changed(self, time_ticks, state):
        #self.pulse_count += self.direction
        time_diff=time_ticks-self.last
        self.last=time_ticks
        if self.record :
            self.list.append(1.0/time_diff)

    def set_direction(self, direction):
        self.direction = direction



motorr = Motor(forward=27, backward=17)
#motorl = Motor(forward=23, backward=24)

speed = 0.5

motorr.forward(speed)
#motorl.forward(speed)

sleep(0.1)

rotorr = EncoderCounter(7)
#rotorl = EncoderCounter(8)

atexit.register(motorr.stop)

sample=0

while (sample <= 100):

    if sample == 50:
        rotorr.record=True

    if sample == 51:
        rotorr.record=False

#    print("Steps = ", rotor.steps, rotor.value, sample)
    thisr = rotorr.pulse_count

   # print("Steps = ", thisr, thisl, thisr-last, status, sample)
    sample = sample+1
    sleep(0.01)


motorr.stop()
#motorl.stop()

#print(rotorr.list)
#print("Summary", forward, backward, stopped)


[print(round(x)) for x in rotorr.list]

rotorr.list
