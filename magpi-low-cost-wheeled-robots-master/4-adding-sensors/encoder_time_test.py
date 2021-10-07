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
        dir(self.device.pin)
 
    def when_changed(self, time_ticks, state):
        #self.pulse_count += self.direction
        time_diff=time_ticks-self.last
        self.last=time_ticks
        if self.record :
            self.list.append(time_diff)

    def set_direction(self, direction):
        self.direction = direction



motorr = Motor(forward=27, backward=17)
#motorl = Motor(forward=23, backward=24)

rotorr = EncoderCounter(7)
print(rotorr.device.pin.edges)
rotorr.device.pin.edges='rising'
print(rotorr.device.pin.edges)
#quit()

speed = 0.5

motorr.forward(speed)
#motorl.forward(speed)

sleep(0.1)



#rotorl = EncoderCounter(8)

atexit.register(motorr.stop)

sample=0

start_time=time.time()
stop_at_time=start_time+1
true_start=start_time+0.5
true_end=start_time+0.51
#while (sample <= 100):
while time.time() < stop_at_time:

    #if sample == 50:
    now=time.time()
    rotorr.record=now >= true_start and now < true_end
#        rotorr.record=True

#    if sample == 51:
#        rotorr.record=False

#    print("Steps = ", rotor.steps, rotor.value, sample)
    thisr = rotorr.pulse_count

   # print("Steps = ", thisr, thisl, thisr-last, status, sample)
    sample = sample+1
    sleep(0.01)


motorr.stop()
#motorl.stop()

#print(rotorr.list)
#print("Summary", forward, backward, stopped)


[print((x)) for x in rotorr.list]

sum=0
for x in rotorr.list:
    sum+=x

sum/=len(rotorr.list)

rotorr.list
print("Mean", sum)

quit()
