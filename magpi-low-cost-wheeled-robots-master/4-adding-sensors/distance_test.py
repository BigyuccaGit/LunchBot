from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED
from gpiozero.tools import booleanized
from signal import pause

threshold_distance=0.3
 
lsensor = DistanceSensor(echo=5,  trigger=6,  threshold_distance=threshold_distance, queue_len=4)
rsensor = DistanceSensor(echo=13, trigger=26, threshold_distance=threshold_distance, queue_len=4)
ledl=LED(12)
ledr=LED(16)

#while True:

#    print('Distance to nearest l object is', lsensor.distance*100, "cm ", lsensor.value)
#    if lsensor.value < threshold_distance:
#        ledl.on()
#    else:
#        ledl.off()

#    ledl.value=lsensor.value < threshold_distance

#    print('Distance to nearest r object is', rsensor.distance*100, 'cm ', rsensor.value)
#    if rsensor.value < threshold_distance:
#        ledr.on()
#    else:
#        ledr.off()
#    ledr.value=rsensor.value < threshold_distance
#    sleep(0.01)

ledl.source=booleanized(lsensor,0,threshold_distance)
ledr.source=booleanized(rsensor,0,threshold_distance)

pause()
