import time
import threading

class BackgroundTask(threading.Thread):

    def __init__(self, func, id, daemon=True, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.func = func
        self.id = id
            
    def run(self,*args,**kwargs):
        self.t=time.time()
        while True:
            self.t += 0.1
            self.func()
            interval=max(self.t-time.time(),0)
           # print(self.id, interval)
            time.sleep(interval)
  
