from approxeng.input.selectbinder import ControllerResource

class HomePressed(Exception):
    pass

try:
    while True:
        try:
            with ControllerResource() as joystick:
                print('Found a joystick and connected')
                while joystick.connected:
                    # Get a corrected value for the left stick x-axis
                    left_x = joystick['lx']
                    # We can also get values as attributes:
                    left_y = joystick.ly
                    
                    right_x = joystick.rx
                    right_y = joystick.ry
                
                    #print("x,y = (",left_x,left_y,")", "(",right_x,right_y,")")
                
                    joystick.check_presses()

                    # If home was pressed, raise a RobotStopException to bail out of the loop
                    # Home is generally the PS button for playstation controllers, XBox for XBox etc

                    if joystick.has_presses:
                        print("Pressed")
                        print(joystick.presses)
                    
                    if joystick.presses.home:
                        raise HomePressed()
                        #exit()

                        # Joystick disconnected...
                        print('Connection to joystick lost')
        except IOError:
            # No joystick found, wait for a bit before trying again
            print('Unable to find any joysticks')
            sleep(1.0)
            
except HomePressed:
    print("Home pressed")
           

