from gpiozero import DigitalInputDevice
import time
import threading

class EncoderCounter():
    class BackgroundTasks(threading.Thread):
        def __init__(self, func, *args, **kwargs):
            super().__init__(*args,**kwargs)
            self.func = func
            
        def run(self,*args,**kwargs):
          t=time.time()
          while True:
              t += 0.1
              self.func()
            #  print('Hello', time.time())
              time.sleep(t-time.time())
              
    def calc_delta(self):
        self.pulse_delta = self.pulse_count - self.pulse_last
        self.pulse_last = self.pulse_count    
 
    def __init__(self, pin_number):
        self.pulse_count = 0
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.when_changed = self.when_changed
        self.direction = 1
        self.last=0
        self.pulse_last=0
        self.record=False
        self.list=[]
        self.pulse_delta=0
        #print(dir(self.device.pin))
        self.last_pulse_count=0

        self.t = EncoderCounter.BackgroundTasks(self.calc_delta, daemon=True)
        self.t.start()

    def when_changed(self, time_ticks, state):
        time_diff=time_ticks-self.last
        self.last=time_ticks
  #      if self.record :
  #          self.list.append(time_diff)
        self.pulse_count += self.direction

    def set_direction(self, direction):
        self.direction = direction

       

 
