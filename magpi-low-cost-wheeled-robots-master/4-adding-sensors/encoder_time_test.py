from gpiozero import Motor
from time import sleep
import atexit
#from gpiozero import DigitalInputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor, DistanceSensorNoEcho
from encoder_counter import EncoderCounter
import time
import logging
import sys
#import vpython as vp

def exit_all():
  motorr.stop()
  motorl.stop()
  sleep(1.0)
  
file_handler = logging.FileHandler(filename='test_encoder.log',mode='w')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(level=logging.INFO, handlers=handlers, format='%(message)s')

  

logger = logging.getLogger("test_encoder")

motorl = Motor(forward=24, backward=23)
motorr = Motor(forward=27, backward=17)

rotorl = EncoderCounter(8,'L')
rotorr = EncoderCounter(7,'R')

factory = PiGPIOFactory()
 
lsensor = DistanceSensor(echo=13, trigger=26, queue_len=2,
                                                   pin_factory=factory)
rsensor = DistanceSensor(echo=5, trigger=6, queue_len=2,
                                                    pin_factory=factory)


print(rotorl.device.pin.edges, rotorr.device.pin.edges )

#quit()

speed = 1
atexit.register(exit_all)



sample=0


start_time=time.time()
stop_at_time=start_time+5

#print("vp.graph")
#vp.graph(xmin=0, xmax=10, scroll=True)
#print("temp_graph")
#temp_graph=vp.gcurve()

motorr.forward(speed)
motorl.forward(speed)

sleep(0.1)

t=time.time()
while time.time() < stop_at_time:
     t = t + 0.1
#     print(time.time(), rotorl.pulse_count, rotorl.pulse_last, rotorl.pulse_delta, rotorr.pulse_count, rotorr.pulse_last, rotorr.pulse_delta)
#     print(time.time(), rotorr.pulse_count, rotorr.pulse_delta)
     elapsed = time.time()-start_time
#     print( f"dummy {elapsed}")
     logger.info(f"{elapsed:.2f} {rotorl.pulse_delta:10d} {rotorl.pulse_delta2:4d} {rotorl.smoothed_pulse_delta:6d} {rotorl.smoothed_pulse_delta2:4d} {lsensor.distance*100:6.1f} {rotorr.pulse_delta:10d} {rotorl.pulse_delta2:4d} {rotorr.smoothed_pulse_delta:6d} {rotorr.smoothed_pulse_delta2:4d} {rsensor.distance*100:6.1f}")
           
 #    vp.rate(10)
 #    temp.graph.plot(elapsed, smoothed_pulse_delta)
  #   sleep(0.2)
     sleep(max(0,t - time.time()))

exit_all()

