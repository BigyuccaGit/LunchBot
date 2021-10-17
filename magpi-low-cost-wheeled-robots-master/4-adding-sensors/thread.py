import threading
import time
from signal import pause

class BackgroundTasks(threading.Thread):
    def run(self,*args,**kwargs):
        t=time.time()
        while True:
            t += 1
            print('Hello', time.time())
            time.sleep(t-time.time())

t = BackgroundTasks(daemon=True)
t.start()
pause()

