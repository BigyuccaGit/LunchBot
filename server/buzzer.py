from gpiozero import Buzzer
from time import sleep
from pins import *

bz = Buzzer(BUZZER_PIN)

try:
    bz.on()
    sleep(1.0)
except KeyboardInterrupt:
    bz.off()


