import subprocess

class RobotModes(object):
    """Our robot behaviors and tests as running modes"""

    # Mode config goes from a "mode_name" to a script to run. Configured for look up.

    mode_config = {
        "buzzer":   {"script": "buzzer.py", "server": False},
        "left_led": {"script": "left_led.py", "server": False},
        "right_led": {"script": "right_led.py", "server": False},
        "backwards": {"script": "backwards.py","server": False}
#        "test_rainbow": "test_rainbow.py",
#        "straight_line": "straight_line_drive.py",
#        "square": "drive_square.py",
#        "line_following": "line_follow_behavior.py",
#        "color_track": "color_track_behavior.py",
#        "face_track": "face_track_behavior.py",
    }


    menu_config = [
        {"mode_name": "buzzer", "text": "Sound Buzzer"},
        {"mode_name": "left_led", "text": "Left LED"},
        {"mode_name": "right_led", "text": "Right LED"},
        {"mode_name": "backwards", "text": "Backwards"},
#        {"mode_name": "line_following", "text": "Line Following"},
#       {"mode_name": "color_track", "text": "Color Tracking"},
#        {"mode_name": "face_track", "text": "Face Tracking"},
#        {"mode_name": "manual_drive", "text": "Drive Manually"},
#        {"mode_name": "behavior_line", "text": "Drive In A Line"},
#        {"mode_name": "drive_north", "text": "Drive North"}
   ]

    # Set up the current process
    def __init__(self):
        self.current_process = None

    # Check if there is a process running. 
    def is_running(self):
       #  Return code is only set when a process finishes.
        return self.current_process and self.current_process.returncode is None
    
    # Run the mode as a subprocess, but not if we still have one running
    def run(self, mode_name):
        """Run the mode as a subprocess, but not if we still have one running"""
        while self.is_running():
            self.stop()

        script = self.mode_config[mode_name]['script']
        self.current_process = subprocess.Popen(["python3", script])

    # Stop a process
    def stop(self):
        if self.is_running():
            # Sending the signal sigint is (on Linux) similar to pressing ctrl-c.
            # That causes the behavior to clean up and exit.
            self.current_process.send_signal(subprocess.signal.SIGINT)
            self.current_process = None

    # Should we redirect?
    def should_redirect(self, mode_name):
        return self.mode_config[mode_name].get('server') is True and self.is_running()
