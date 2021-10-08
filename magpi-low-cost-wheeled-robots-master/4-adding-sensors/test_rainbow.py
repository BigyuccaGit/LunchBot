from time import sleep
from leds_led_shim import Leds
from led_rainbow import show_rainbow

leds = Leds()

offset=0
while True:
#    print("on")
    show_rainbow(offset, leds, range(leds.count))
    offset += 1
    leds.show()
    sleep(0.1)
    #print("off")
    #leds.clear()
    #leds.show()
    #sleep(0.5)
