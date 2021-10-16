from robot import Robot, DistanceSensorNoEcho
import atexit
from time import sleep
import random
import logging
import sys


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
        
       # Ensure it will stop
        atexit.register(self.robot.stop_all)

    def backwards(self):
        self.robot.backward()
        if self.buzzer_enabled:
            self.buzzer.beep(0.2,0.2)
        sleep(1.0)
        self.robot.stop()    
        if self.buzzer_enabled:
            self.buzzer.off()
        
    def right_spin(self):
        logger.info("RIGHT SPIN")
        self.robot.speeds(100,-100)
        sleep(1.0)
        self.robot.stop()
  
    def left_spin(self):
        logger.info("LEFT SPIN")
        self.robot.speeds(-100,100)
        sleep(1.0)
        self.robot.stop()
  
    def random_spin(self):
        heads_or_tails = random.randint(0,1)
        [self.left_spin, self.right_spin][heads_or_tails]()

    def choose_spin(self, r_in_range, l_in_range):
        option = (r_in_range << 1) + l_in_range
        return [self.random_spin, self.right_spin, self.left_spin, self.random_spin][option]
#                 failsafe,         left sensor,     right sensor,     both sensors

    def run(self):

        logging.basicConfig(level=logging.INFO, handlers=handlers, format='%(name)s %(levelname)s:%(asctime)s %(message)s')
        
        while True:
            
            # Send robot forward
            logger.info(f"FORWARD {self.r_sensor.in_range} {self.r_sensor.distance*100} {self.l_sensor.in_range} {self.l_sensor.distance*100}")
            self.robot.forward()

            # Wait for object to come in range
            while not self.r_sensor.in_range and not self.l_sensor.in_range: 
                sleep(0.01) 

            # Stop the robot
            self.robot.stop()
            logger.info("STOP")

            # Choose which spin option to do in a moment based on current settings
            self.spin_option=self.choose_spin(self.r_sensor.in_range, self.l_sensor.in_range)

            # Go Backwards
            logger.info("BACKWARD")
            self.backwards()

            # Execute chosen spin option
            logger.info("SPIN")
            
            self.spin_option()    

bot=Robot()
behaviour=ObstacleAvoidance(bot)
behaviour.buzzer_enabled = False

behaviour.run()
