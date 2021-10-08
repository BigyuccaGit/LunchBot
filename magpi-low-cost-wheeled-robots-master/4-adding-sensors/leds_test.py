from leds_led_shim import Leds
from time import sleep

leds = Leds()
red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    print("red")
    leds.set_all(red)
    leds.show()
    sleep(0.5)
    print("blue")
    leds.set_all(blue)
    leds.show()
    sleep(0.5)
