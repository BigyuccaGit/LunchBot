from gpiozero import LED
from time import sleep
from pins import *

led = LED(R_LED_PIN)

try:
    led.on()
    sleep(1.0)
except KeyboardInterrupt:
    led.off()



