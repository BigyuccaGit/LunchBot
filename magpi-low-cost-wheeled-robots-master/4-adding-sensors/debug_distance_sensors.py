from gpiozero import DistanceSensor, LED
from signal import pause

left_sensor = DistanceSensor(echo=5, trigger=6, max_distance=1, threshold_distance=0.1)
right_sensor = DistanceSensor(echo=13, trigger=26, max_distance=1, threshold_distance=0.11)

left_sensor.when_in_range = lambda: print("Left obstacle in range")
left_sensor.when_out_of_range = lambda: print("Left obstacle out of range")

right_sensor.when_in_range = lambda: print("Right obstacle in range")
right_sensor.when_out_of_range = lambda: print("Right obstacle out of range")


pause()
