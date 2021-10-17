from gpiozero import Motor
from time import sleep
import atexit
#from gpiozero import DigitalInputDevice

from encoder_counter import EncoderCounter
import time
import logging

logger = logging.getLogger("test_encoders")

motorr = Motor(forward=27, backward=17)
#motorl = Motor(forward=23, backward=24)

rotorr = EncoderCounter(7)
print(rotorr.device.pin.edges)
rotorr.device.pin.edges='rising'
print(rotorr.device.pin.edges)
#quit()

speed = 1

motorr.forward(speed)
#motorl.forward(speed)

sleep(0.1)


#rotorl = EncoderCounter(8)

atexit.register(motorr.stop)

sample=0

start_time=time.time()
stop_at_time=start_time+20
true_start=start_time+0.5
true_end=start_time+5.5
#while (sample <= 100):
while time.time() < stop_at_time:

    #if sample == 50:
#    now=time.time()
#   rotorr.record=now >= true_start and now < true_end
#        rotorr.record=True

#    if sample == 51:
#        rotorr.record=False

#    print("Steps = ", rotor.steps, rotor.value, sample)
#    rotorr.pulse_count

   # print("Steps = ", thisr, thisl, thisr-last, status, sample)
 #   sample = sample+1
     print(time.time(), rotorr.pulse_count, rotorr.pulse_delta)
     sleep(0.1)


motorr.stop()
#motorl.stop()

#print(rotorr.list)
#print("Summary", forward, backward, stopped)


#[print((x)) for x in rotorr.list]

#sum=0
#for x in rotorr.list:
#    sum+=x
    
#print("sum", sum, rotorr.pulse_count)


#sum/=len(rotorr.list)

#rotorr.list
#print("Mean", sum)

#quit()
