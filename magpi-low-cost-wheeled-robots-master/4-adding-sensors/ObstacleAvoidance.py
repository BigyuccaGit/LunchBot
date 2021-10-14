from robot import Robot, DistanceSensorNoEcho

class ObstacleAvoidance:

    def __init__(self, the_robot):
        
        self.robot = the_robot
        # Ensure it will stop
        atexit.register(self.robot.stop_all)
        self.r_sensor.robot.right_distance_sensor
        self.l_sensor.robot.left_distance_sensor

    def backwards(self):
        self.robot.backward()
        sleep(1.0)
        self.robot.stop()    
  
    def right_spin(self):
        print("RIGHT SPIN")
        self.robot.speeds(100,-100)
        #self.robot.right_motor.backward()
        sleep(1.0)
        self.robot.stop()
  
    def left_spin(self):
        print("LEFT SPIN")
        rself.robot.speeds(-100,100)
        #self.robot.right_motor.forward()
        #self.robot.left_motor.backward()
        sleep(1.0)
        self.robot.stop()
  
    self.coin_toss=[self.left_spin, self.right_spin]
    def random_spin(self):
        self.coin_toss[random.randint(0,1)]()

    self.spin_options=[self.random_spin, self.right_spin, self.left_spin, self.random_spin]
    #                 failsafe,   left sensor, right sensor, both sensors
    def choose_spin(self, r_in_range, l_in_range):
        option = (r_in_range << 1) + l_in_range
        #spin_option[option]()
        print(r_in_range, l_in_range, option)
        return spin_options[option]
  

    def run(self):
        while True:
              # Send robot forward
            print("FORWARD")
            self.robot.forward()
            print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)

            # Wait for object to come in range
            while not self.r_sensor.in_range and not self.l_sensor.in_range: 
                #  print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)
                sleep(0.01) 

            # Stop the robot
            self.robot.stop()
            print("STOP")

            # Choose which spin option to do in a moment based on current settings
            self.spin_option=choose_spin(self.r_sensor.in_range, self.l_sensor.in_range)

            # Go Backwards
            print("BACKWARD")
            self.backwards()  

            # Execute chosen spin option
            print("SPIN")
            self.spin_option()    

bot=Robot()
behaviour=ObstableAvoidance(bot)
begaviour.run()
