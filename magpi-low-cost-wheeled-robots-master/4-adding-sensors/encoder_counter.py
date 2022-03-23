from gpiozero import DigitalInputDevice
import atexit
from background_task import BackgroundTask

class EncoderCounter():
              
    def __init__(self, pin_number, id, interval=0.1, buffer_delta_size=5, buffer_delta2_size=5):
        # Initiate encoder and only trigger on rising edge
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.edges='rising'

        # Some starting values
        self.pulse_count = 0
        self.direction = 1
#        self.pulse_last = 0
#        self.pulse_delta = 0
#        self.pulse_delta_last = 0
#        self.pulse_delta2=0

        # Set up smoothing buffers
#        self.buffer_delta_size = buffer_delta_size
#        self.buffer_delta_index = 0
#        self.buffer_delta = buffer_delta_size * [0]
#        self.buffer_delta2_size = buffer_delta2_size
#        self.buffer_delta2_index = 0
#        self.buffer_delta2 = buffer_delta2_size * [0]

        # ID which encoder
        self.id = id

        # Set up background counting of encoder pulse count
        self.device.pin.when_changed = self.when_changed

        # Set up and start background daemon thread that calculates delta and delta2 pulse counts every# 'interval' seconds
#        self.thread = BackgroundTask(self.background_calc_pulse_delta, interval, self.id)
#        self.thread.start()
        #print("Daemon = ", self.thread.daemon)
 
    # Define method to run in background thread.
    # Calculates delta and delta2 encoder pulse counts as proxy for speed and acceleration
#    def background_calc_pulse_delta(self):

#        # Calculate one delta pulse count
#        pc = self.pulse_count
#        self.pulse_delta = pc - self.pulse_last
#        self.pulse_delta2 = self.pulse_delta-self.pulse_delta_last
        
        # Store delta pulse count in smoothing delta buffer and move rotating index
#        self.buffer_delta[self.buffer_delta_index] = self.pulse_delta
#        self.buffer_delta_index = (self.buffer_delta_index + 1) % self.buffer_delta_size
       #      print(self.id, self.pulse_delta, self.pulse_count, self.pulse_last)
      
        # Store delta2 pulse count in smoothing delta2 buffer and move rotating index
#        self.buffer_delta2[self.buffer_delta2_index] = self.pulse_delta2
#        self.buffer_delta2_index = (self.buffer_delta2_index + 1) % self.buffer_delta2_size

        # Remember values for next call
#        self.pulse_last = pc
#        self.pulse_delta_last = self.pulse_delta
 
    # Returns smoothed delta pulse count as property
#    @property
#    def smoothed_pulse_delta(self):
#        return sum(self.buffer_delta)
    
    # Returns smoothed delta2 pulse count as property
#    @property
#    def smoothed_pulse_delta2(self):
#        return sum(self.buffer_delta2)

    # Define method called on detection of pulse count
    def when_changed(self, _, state):
        self.pulse_count += self.direction

    # Defines direction we are going (1 = forward)
    def set_direction(self, direction):
        self.direction = direction

    # Shutdown
    def stop_all(self):
        self.device.pin.when_changed = None
        

       

 
