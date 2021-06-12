import multiprocessing
import time

"""

"""
def Evennum(t):
    time.sleep(10 - t)
    print(multiprocessing.current_process().name)

processes = []
for i in range(10):
    processes.append(multiprocessing.Process(target=Evennum, args=(i,), daemon=True))

for p in processes:
    p.start()

for process in processes:
    print(process.name, " JOIN")
    #process.join()


import os
os.system('ps aux| grep python')

time.sleep(5)
os.system('ps aux| grep python')
