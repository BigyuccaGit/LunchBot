import time
import threading

class BackgroundTask(threading.Thread):

    def __init__(self, func, interval, id, daemon=True, *args, **kwargs):
        super().__init__(daemon=daemon,*args,**kwargs)
        self.func = func
        self.interval = interval
        self.id = id
            
    def run(self,*args,**kwargs):
        self.t=time.time()
        while True:
            self.t += self.interval
            self.func()
            interval=max(self.t-time.time(),0)
           # print(self.id, interval)
            time.sleep(interval)
  
