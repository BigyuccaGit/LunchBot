import subprocess
import csv

class RobotModes(object):
    """Our robot behaviors and tests as running modes"""
 
    # Set up the current process and load menu information from csv format file
    def __init__(self):
        self.current_process = None

        self.mode_config = {}
        self.menu_config = []
        filename="robot_modes.dat"
        with open(filename) as file:
            reader=csv.reader(file)
            line = 0;
            for row in reader:
                if line > 0:        
                    server=row[3].strip() == "True"
                    script = row[2].lstrip().rstrip()
                    subdict = {"script": script, "server": server}
                    self.mode_config[row[0]] = subdict

                    mode_name = row[0].lstrip().rstrip()
                    text = row[1].lstrip().rstrip()
                    subdict = {"mode_name": mode_name, "text" : text}
                    self.menu_config.append(subdict)
                line = line + 1

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


