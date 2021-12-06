from robot import Robot, DistanceSensorNoEcho
import atexit
from time import sleep
import time
import random
import logging
import sys
from icm20948 import ICM20948
import math
from robot_imu import RobotImu
from delta_timer import DeltaTimer
import imu_settings

file_handler = logging.FileHandler(filename='robot.log',mode='w')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logger=logging.getLogger("ObstacleAvoidance")
 
class ObstacleAvoidance:

    def __init__(self, the_robot):
        
        self.robot = the_robot
        self.r_sensor = self.robot.right_distance_sensor
        self.l_sensor = self.robot.left_distance_sensor
        self.buzzer = self.robot.buzzer
        self.buzzer_enabled = True
        self.r_led = self.robot.right_led
        self.l_led = self.robot.left_led
        # Calcs for LEDs
        self.led_half = int(self.robot.leds.count/2)
        self.sense_colour = 255,0,0
        self.imu = ICM20948()
        self.acc_threshold = 3.0
        self.acc_threshold_mag = self.acc_threshold * self.acc_threshold
        self.collided = False
        self.robot_imu = RobotImu(mag_offsets=imu_settings.mag_offsets,
               gyro_offsets=imu_settings.gyro_offsets)
        self.delta = DeltaTimer()
        self.spin_angle = 90 + 45
        self.slow_spin_speed = 60
        
       # Ensure it will stop
        atexit.register(self.robot.stop_all)

    # Distance to number LEDs
    def distance_to_led_bar(self, distance):
        # Invert so closer means more LEDs
        inverted = max(1.0 - distance, 0)
        led_bar = int(round(inverted * self.led_half))
        return led_bar

    # Create the 2 bars on the LED SHIM
    def display_state(self, left_distance, right_distance):
        # Clear first
#        self.robot.leds.clear()
        # Left side
#        l_led_bar = self.distance_to_led_bar(left_distance)
#        self.robot.leds.set_range(range(l_led_bar), self.sense_colour)
        # Right side
#        r_led_bar = self.distance_to_led_bar(right_distance)
#        start = (self.robot.leds.count - 1) - r_led_bar
        #logger.info(f"LEDS  {l_led_bar} ({left_distance*100:.0f}) {r_led_bar} ({right_distance*100:.0f}) {collided}")
#        logger.info(f"TEST  ({left_distance*100:.0f}) ({right_distance*100:.0f})")

#        self.robot.leds.set_range(range(start, self.robot.leds.count-1), self.sense_colour)
        # Now show
#        self.robot.leds.show()
        None

    # Have we collided with something
    def colliding(self):
        if not self.collided:
            ax, ay, az, _, _, _ = self.imu.read_accelerometer_gyro_data()
            amag=ax*ax + ay*ay + az*az
            self.collided = amag > self.acc_threshold_mag
            if self.collided:
                print("COLLIDED", amag)
        return self.collided
        
    def backwards(self):
        self.robot.backward()
        if self.buzzer_enabled:
            self.buzzer.beep(0.2,0.2)
        sleep(1.0)
        self.robot.stop()    
        if self.buzzer_enabled:
            self.buzzer.off()
        
#    def right_spin(self):
#        logger.info("RIGHT SPIN")
#        self.robot.speeds(100,-100)
#        sleep(1.0)
#        self.robot.stop()

    def right_spin(self):
        
        logger.info("RIGHT SPIN ANGLE")
        self.r_led.blink(0.2, 0.2)
        yaw=0.0
        while -yaw < self.spin_angle:
            sleep(0.001)
            dt,elapsed = self.delta.update()
            gyro=self.robot_imu.read_gyroscope()
            yaw += gyro.z * dt

            if self.spin_angle + yaw > 30:
                speed = 100
            else:
                speed = self.slow_spin_speed
        
            self.robot.speeds(speed, -speed)
            
        self.robot.stop()
        self.r_led.off()

#    def left_spin(self):
#        logger.info("LEFT SPIN")
#        self.robot.speeds(-100,100)
#        sleep(1.0)
#        self.robot.stop()

    def left_spin(self):
        
        logger.info("LEFT SPIN ANGLE")
        self.l_led.blink(0.2, 0.2)
        yaw=0.0
        while yaw < self.spin_angle:
            sleep(0.001)
            dt,elapsed = self.delta.update()
            gyro=self.robot_imu.read_gyroscope()
            yaw += gyro.z * dt

            if self.spin_angle - yaw > 30:
                speed = 100
            else:
                speed = self.slow_spin_speed
            
            self.robot.speeds(-speed, speed)
            
        self.robot.stop()
        self.l_led.off()
    
    def random_spin(self):
        heads_or_tails = random.randint(0,1)
        [self.left_spin, self.right_spin][heads_or_tails]()

    def choose_spin(self, r_in_range, l_in_range):
        option = (r_in_range << 1) + l_in_range
        return [self.random_spin, self.right_spin, self.left_spin, self.random_spin][option]
#                 failsafe,         left sensor,     right sensor,     both sensors

    def run(self):

        logging.basicConfig(level=logging.INFO, handlers=handlers, format='%(name)s %(levelname)s:%(asctime)s %(message)s')
        
        acc_threshold = 3.0
        dt=0.01
        
        while True:
            
            # Send robot forward
            logger.info(f"FORWARD {self.r_sensor.in_range} {self.r_sensor.distance*100:.0f} {self.l_sensor.in_range} {self.l_sensor.distance*100:.0f}")
            self.robot.forward()

            # Wait for object to come in range
            t=time.time()
            inc=0
            while (not self.r_sensor.in_range and not self.l_sensor.in_range) and (not self.colliding()) :
            
#            while (not self.r_sensor.in_range and not self.l_sensor.in_range):
            
                left_distance = self.l_sensor.distance
                right_distance = self.r_sensor.distance

                inc += 1
                if inc % 1 == 0:
                    self.display_state(left_distance, right_distance)#, self.l_sensor.in_range, self.r_sensor.in_range )
                t=t+dt
                sleep(max(0, t-time.time()) ) 

            # Stop the robot
            self.collided = False
            self.robot.stop()
            logger.info("STOP")

            # Choose which spin option to do in a moment based on current settings
            if self.collided:
                 self.spin_option=self.choose_spin(0, 0)
            else:
               self.spin_option=self.choose_spin(self.r_sensor.in_range, self.l_sensor.in_range)

            # Go Backwards
            logger.info("BACKWARD")
            self.backwards()

            # Execute chosen spin option
            logger.info("SPIN")
            
            self.spin_option()    

bot=Robot(encoder=False)
behaviour=ObstacleAvoidance(bot)
behaviour.buzzer_enabled = False

behaviour.run()
