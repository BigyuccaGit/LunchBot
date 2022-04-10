from approxeng.input.selectbinder import ControllerResource
from pins import *
from gpiozero import Buzzer, LED

class HomePressed(Exception):
    pass


buzzer=Buzzer(BUZZER_PIN)
buzzer.off()

r_led=LED(R_LED_PIN)
r_led.off()
l_led=LED(L_LED_PIN)
l_led.off()

sq_count=0

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

                    if joystick.presses.circle:
                        print("Circle pressed")
                        buzzer.on()

                    if joystick.releases.circle:
                        print("Circle released")
                        buzzer.off()
                    
                    if joystick.presses.square:
                        print("Square pressed ", sq_count)
                        if r_led.is_lit:
                            r_led.off()
                        else:
                            r_led.on()
                            
                        if l_led.is_lit:
                            l_led.off()
                        else:
                            l_led.on()

                        sq_count += 1
                    
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
    buzzer.off()
    r_led.off()
    l_led.off()
           

