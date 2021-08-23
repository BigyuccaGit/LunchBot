from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED
from gpiozero.tools import booleanized
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
       
factory = PiGPIOFactory()
threshold_distance_cm=10
hysteresis_cm=0

threshold_distance=threshold_distance_cm/100.0
hysteresis=hysteresis_cm/100.0

rsensor = DistanceSensor(echo=5,  trigger=6,  threshold_distance=threshold_distance, queue_len=4, pin_factory=factory)
lsensor = DistanceSensor(echo=13, trigger=26, threshold_distance=threshold_distance, queue_len=9, pin_factory=factory)
#ledl=LED(12)
#ledr=LED(16)

while True:

#    print('Distance to nearest l object is', lsensor.distance*100, "cm ", lsensor.value)
#    if lsensor.value < threshold_distance:
#        ledl.on()
#    else:
#        ledl.off()

#    ledl.value=lsensor.value < threshold_distance
    x=booleanized(rsensor,threshold_distance,1,hysteresis=hysteresis) 
    y=booleanized(lsensor,threshold_distance,1,hysteresis=hysteresis) 
 
    dist=f'{rsensor.distance*100:.3f} cm'
    print('Distance to nearest r object is '+ dist, next(x) )
    dist=f'{lsensor.distance*100:.3f} cm'
    print('Distance to nearest l object is '+ dist, next(y) )
#    if rsensor.value < threshold_distance:
#        ledr.on()
#    else:
#        ledr.off()
#    ledr.value=rsensor.value < threshold_distance
    sleep(0.01)

#ledl.source=booleanized(lsensor,0,threshold_distance)
#ledr.source=booleanized(rsensor,0,threshold_distance)

pause()


