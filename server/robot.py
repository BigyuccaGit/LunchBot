import gpiozero 
import atexit
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor, DistanceSensorNoEcho
from gpiozero import LED, Buzzer
import leds_led_shim
from encoder_counter import EncoderCounter
from pins import *

class Robot:
    def __init__(self, distance = True, encoder = True):

        # Setup the motors
        self.left_motor= gpiozero.Motor(forward=L_MOTOR_F_PIN, backward=L_MOTOR_B_PIN)
        self.right_motor = gpiozero.Motor(forward=R_MOTOR_F_PIN, backward=R_MOTOR_B_PIN)

        # Setup the Distance Sensors
        if distance :
            factory = PiGPIOFactory()
            self.left_distance_sensor = DistanceSensor(\
                                                   echo=L_SENSOR_ECHO_PIN ,\
                                                   trigger=L_SENSOR_TRIGGER_PIN ,\
                                                   queue_len=2, \
                                                   pin_factory=factory)
            self.right_distance_sensor = DistanceSensor(echo=R_SENSOR_ECHO_PIN,\
                                                    trigger=R_SENSOR_TRIGGER_PIN,\
                                                    queue_len=2,
                                                    pin_factory=factory)
        else:
             self.left_distance_sensor = None
             self.right_distance_sensor = None
            
        # Setup the encoders
        if encoder:
            self.left_encoder = EncoderCounter(L_ENCODER_PIN, "L")
            self.right_encoder = EncoderCounter(R_ENCODER_PIN, "R")
        else:
            self.left_encoder = None
            self.right_encoder = None
            
        # Set up the Buzzer
        self.buzzer = Buzzer(BUZZER_PIN )

        # Set up the LEDs
        self.left_led = LED(L_LED_PIN)
        self.right_led = LED(R_LED_PIN)

        # Set up the LED SHIM
        self.leds = leds_led_shim.Leds();

        # Ensure the motors get stopped when the code exits
        atexit.register(self.stop_all)

    def get_operation(self, motor, speed):
        # Choose the operation
        operation = motor.stop
        if speed > 0:
            operation = motor.forward
        elif speed < 0:
            operation = motor.backward
        
        return operation

    def perform(self, operation, speed):
        if speed != 0:
  #          print("Calling non stop", speed)
            operation(min(abs(speed)/100.0,1.0))
        else:
  #          print("Calling stop")
            operation()
    
    def left_motor_speed(self, speed=100):
        operation = self.get_operation(self.left_motor, speed)
        self.perform(operation, speed)

    set_left=left_motor_speed
    
    def right_motor_speed(self, speed=100):
        operation = self.get_operation(self.right_motor, speed)
        self.perform(operation, speed)

    set_right=right_motor_speed
    
    def speeds(self, left_speed=100, right_speed=100):
        self.left_motor_speed(left_speed)
        self.right_motor_speed(right_speed)
        
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def forward(self, speed=100):
        self.left_motor_speed(speed)
        self.right_motor_speed(speed)

    def backward(self, speed=100):
        self.left_motor_speed(-speed)
        self.right_motor_speed(-speed)

    def stop_all(self):
        self.stop()
        self.buzzer.off()
        self.right_led.off()
        self.left_led.off()
        self.leds.clear()
        self.leds.show()

        # add any more h/ww stops here
  
        
