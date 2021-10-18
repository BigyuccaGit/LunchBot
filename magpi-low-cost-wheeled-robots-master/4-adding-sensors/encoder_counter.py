from gpiozero import DigitalInputDevice
import atexit
from background_task import BackgroundTask

class EncoderCounter():
              
    def __init__(self, pin_number, id):
        self.pulse_count = 0
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.edges='rising'
        self.direction = 1
        self.pulse_last=-1
        self.pulse_delta=0
        self.id = id
        
        self.device.pin.when_changed = self.when_changed
        self.t = BackgroundTask(self.calc_delta, self.id)
        self.t.start()
        
    def calc_delta(self):
        self.pulse_delta = self.pulse_count - self.pulse_last
  #      print(self.id, self.pulse_delta, self.pulse_count, self.pulse_last)
        self.pulse_last = self.pulse_count    
       
    def when_changed(self, time_ticks, state):
        self.pulse_count += self.direction

    def set_direction(self, direction):
        self.direction = direction

    def stop_all(self):
        self.device.pin.when_changed = None
        

       

 
