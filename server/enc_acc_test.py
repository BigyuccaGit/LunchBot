from gpiozero import Motor
from time import sleep
import atexit
#from gpiozero import DigitalInputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor, DistanceSensorNoEcho
from encoder_counter import EncoderCounter
from icm20948 import ICM20948
import time
import logging
import sys
from pins import *

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

motorl = Motor(forward=L_MOTOR_F_PIN, backward=L_MOTOR_B_PIN)
motorr = Motor(forward=R_MOTOR_F_PIN, backward=R_MOTOR_B_PIN)

rotorl = EncoderCounter(R_ENCODER_PI,'L')
rotorr = EncoderCounter(L_ENCODER_PIN,'R')

factory = PiGPIOFactory()
 
lsensor = DistanceSensor(echo=L_SENSOR_ECHO_PIN, trigger=L_SENSOR_TRIGGER_PIN, queue_len=2,
                                                   pin_factory=factory)
rsensor = DistanceSensor(echo=R_SENSOR_ECHO_PIN, trigger=R_SENSOR_TRIGGER_PIN, queue_len=2,
                                                    pin_factory=factory)
imu = ICM20948()

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

     ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
     amag=sqrt(ax*ax + ay*ay + az*az)

     logger.info(f"{elapsed:.2f} {rotorl.pulse_delta:10d} {rotorl.pulse_delta2:4d} {rotorl.smoothed_pulse_delta:6d} {rotorl.smoothed_pulse_delta2:4d} {lsensor.distance*100:6.1f} {rotorr.pulse_delta:10d} {rotorl.pulse_delta2:4d} {rotorr.smoothed_pulse_delta:6d} {rotorr.smoothed_pulse_delta2:4d} {rsensor.distance*100:6.1f}    {amag:5.2f} {ax:5.2f} {ay:5.2f} {az:5.2f} }")
           
 #    vp.rate(10)
 #    temp.graph.plot(elapsed, smoothed_pulse_delta)
  #   sleep(0.2)
     sleep(max(0,t - time.time()))

exit_all()

