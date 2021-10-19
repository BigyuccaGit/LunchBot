import time
import threading

# Class to setup a background thread
class BackgroundTask(threading.Thread):

    # Initiliase ('func' = function to run at time intervals in secs of 'interval')
    def __init__(self, func, interval, id, daemon=True, *args, **kwargs):
        super().__init__(daemon=daemon,*args,**kwargs)
        self.func = func
        self.interval = interval
        self.id = id

    # Run the background thread
    def run(self,*args,**kwargs):

        # Get 1st time
        self.t=time.time()

        # Start infinite loop
        while True:
            # Determine interval for next time to run 'func'
            self.t += self.interval

            # Run 'func'
            self.func()

            # Delay appropriate amount
            interval=max(self.t-time.time(),0)
            time.sleep(interval)
            # print(self.id, interval)
 
