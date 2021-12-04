import time
import threading

# Class to setup a background thread
class BackgroundTask(threading.Thread):

    # Initiliase ('func' = function to run at time intervals in secs of 'interval')
    def __init__(self, func, interval, id, daemon=True, *args):
        super().__init__(daemon=daemon)
        self.func = func
        self.interval = interval
        self.id = id
        self.event=threading.Event()
        self.event.set()
        self.ok = True
        self.start_time = 0
        self.interval=interval
        self.times=[]
        self.args = args
        print("Args", args)

    # Setup task to run in the background thread
    def run(self):
        print("args", self.args)

        # Get 1st time
        self.t=time.time()
        self.start_time = self.t

        # Start infinite loop
        while True:
            #self.event.wait()
            # Determine next time to run 'func'
            self.t += self.interval

            #if self.ok:
                # Run 'func'
            #print("Func",self.t-self.start_time)
            if self.ok:
                self.times.append(round(self.t-self.start_time,3))
                self.func()
                
            # Delay appropriate amount
            interval=max(self.t-time.time(),0)
            time.sleep(interval)
           # print(self.id, interval)

    def suspend(self):
        if self.ok:
        #if self.event.is_set():
         #   self.event.clear()
            self.ok = False
            
    def release(self):
        if not self.ok:
        #if not self.event.is_set():
            self.t=self.start_time + ((time.time()-self.start_time)//self.interval)*self.interval
            self.ok = True
            #  self.event.set()

    def dump(self):
        print(self.times)
     
        
 
