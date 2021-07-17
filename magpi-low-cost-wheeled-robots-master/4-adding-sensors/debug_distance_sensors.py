from gpiozero import DistanceSensor, LED
from signal import pause

sensor = DistanceSensor(echo=5, trigger=6, max_distance=1, threshold_distance=0.2)
led = LED(16)

sensor.when_in_range = lambda: print("Obstacle in range")
sensor.when_out_of_range = lambda: print("Obstacle out of range")


pause()
