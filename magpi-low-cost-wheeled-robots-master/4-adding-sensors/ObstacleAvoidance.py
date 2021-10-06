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
        self.robot.left_motor.forward()
        self.robot.right_motor.backward()
        sleep(1.0)
        self.robot.stop()
  
    def left_spin(self):
        print("LEFT SPIN")
        self.robot.right_motor.forward()
        self.robot.left_motor.backward()
        sleep(1.0)
        self.robot.stop()
  
    coin_toss=[left_spin, right_spin]
    def random_spin(self):
        coin_toss[random.randint(0,1)]()

    spin_options=[random_spin, right_spin, left_spin, random_spin]
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
            while not r_sensor.in_range and not l_sensor.in_range: 
  
                #  print(r_sensor.in_range, r_sensor.distance*100, l_sensor.in_range, l_sensor.distance*100)
                sleep(0.01) 

                # Stop the robot
                robot.stop()
                print("STOP")

                # Choose which spin option to do in a moment based on current settings
                spin_option=choose_spin(r_sensor.in_range, l_sensor.in_range)

                # Go Backwards
                print("BACKWARD")
                backwards()  

                # Execute chosen spin option
                print("SPIN")
                spin_option()

                

bot=Robot()
behaviour=ObstableAvoidance(bot)
begaviour.run()
