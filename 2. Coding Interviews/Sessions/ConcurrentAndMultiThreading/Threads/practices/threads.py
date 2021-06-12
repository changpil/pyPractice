import threading
import time

def Evennum(t):
    time.sleep(10 - t)
    print(threading.current_thread().name)

threads = []
for i in range(10):
    threads.append(threading.Thread(target=Evennum, args=(i,), daemon=True))

for t in threads:
    t.start()

for thread in threads:
    print(thread.name, " JOIN")
    #thread.join()

import os
os.system('ps aux| grep python')

time.sleep(5)
os.system('ps aux| grep python')