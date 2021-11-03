from gpiozero import Buzzer
from time import sleep
from pins import *
import atexit

bz = Buzzer(BUZZER_PIN)
bz.on()
sleep(1.0)
atexit.register(bz.off)


