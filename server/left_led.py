from gpiozero import LED
from time import sleep
from pins import *

led = LED(L_LED_PIN)
try:
  led.on()
  sleep(1)
except KeyboardInterrupt:
  led.off()


