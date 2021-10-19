from gpiozero import DigitalInputDevice
import atexit
from background_task import BackgroundTask

class EncoderCounter():
              
    def __init__(self, pin_number, id, interval=0.5, buffer_size=3):
        # Initiate encoder and only trigger on rising edge
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.edges='rising'

        # Some starting values
        self.pulse_count = 0
        self.direction = 1
        self.pulse_last = 0
        self.pulse_delta = 0

        # Set up smoothing buffer
        self.buffer_index = 0
        self.buffer = buffer_size * [0]

        # ID which encoder
        self.id = id

        # Set up background counting of encoder pulse count
        self.device.pin.when_changed = self.when_changed

        # Set up and start background daemon thread that calculates delta pulse count every 'interval' seconds
        self.thread = BackgroundTask(self.calc_delta, interval, self.id)
        self.thread.start()
        #print("Daemon = ", self.thread.daemon)
 
    # Define method to run in background thread.
    # Calculates delta encoder pulse count as proxy for speed
    def calc_delta(self):

        # Calculate one delta pulse count
        pc = self.pulse_count
        self.pulse_delta = pc - self.pulse_last
        self.pulse_last = pc

        # Store in smoothing buffer and move rotating index
        self.buffer[self.buffer_index] = self.pulse_delta
        self.buffer_index = (self.buffer_index + 1) % self.buffer_size
        #      print(self.id, self.pulse_delta, self.pulse_count, self.pulse_last)
  
    # Returns smoothed delta pulse count as property
    @property
    def smoothed_pulse_delta(self):
        return sum(self.buffer)

    # Define method called on detection of pulse count
    def when_changed(self, time_ticks, state):
        self.pulse_count += self.direction

    # Defines direction we are going (1 = forward)
    def set_direction(self, direction):
        self.direction = direction

    # Shutdown
    def stop_all(self):
        self.device.pin.when_changed = None
        

       

 
