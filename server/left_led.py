from gpiozero import LED
from time import sleep
from pins import *
import atexit

led = LED(L_LED_PIN)
led.on()
sleep(1.0)
atexit.register(led.off)


