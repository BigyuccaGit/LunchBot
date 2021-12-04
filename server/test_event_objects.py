from background_task import BackgroundTask
from time import sleep

def func():
   None
    
thread = BackgroundTask(func, 0.001, 1, True, 2,3)
thread.start()

sleep(.01)
print("suspend")
thread.suspend()
sleep(.01)
print("release")
thread.release()
sleep(.01)
thread.dump()
