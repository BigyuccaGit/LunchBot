from gpiozero import DistanceSensor, LED
from signal import pause

threshold_distancecm=11 # cm

threshold_distance = threshold_distancecm/100

left_sensor = DistanceSensor(echo=5, trigger=6, max_distance=1, threshold_distance=threshold_distance)
right_sensor = DistanceSensor(echo=13, trigger=26, max_distance=1, threshold_distance=threshold_distance)
 
left_sensor.when_in_range = lambda: print("Left obstacle in range")
left_sensor.when_out_of_range = lambda: print("Left obstacle out of range")

right_sensor.when_in_range = lambda: print("Right obstacle in range")
right_sensor.when_out_of_range = lambda: print("Right obstacle out of range")


pause()
