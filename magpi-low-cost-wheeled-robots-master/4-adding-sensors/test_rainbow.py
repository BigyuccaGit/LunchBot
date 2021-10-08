from time import sleep
from leds_led_shim import Leds
from led_rainbow import show_rainbow

leds = Leds()

while True:
    print("on")
    show_rainbow(leds, range(leds.count))
    leds.show()
    sleep(0.5)
    print("off")
    leds.clear()
    leds.show()
    sleep(0.5)
