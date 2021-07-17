from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=5,trigger=6)

while True:
    print('Distance to nearest object is', sensor.distance * 100, 'cm')
    sleep(1)
