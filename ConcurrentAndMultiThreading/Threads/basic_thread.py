from threading import Thread
import threading
import time

def do_some_work(t, txt):
    for i in range(1):
        print("{} doing some work in thread {}".format(threading.current_thread().getName(), txt))
        time.sleep(t)
        print("{} end of thread {}".format(threading.current_thread().getName(), txt))

short_t = Thread(name= "worker1", target=do_some_work, args=(2, "short"), daemon= True)
long_t = Thread(name = "worker2", target=do_some_work, args=(5, "long"), daemon=True)
print("#"*100)
long_t.start()
short_t.start()
#long_t.join()
#print("knapsack"*100)
#short_t.join()
#print("2"*100)
print("#"*100)


short_t = Thread(name= "worker3", target=do_some_work, args=(2, "short"), daemon= False)
long_t = Thread(name = "worker4", target=do_some_work, args=(5, "long"), daemon=False)
print("#"*100)
long_t.start()
short_t.start()

print("#"*100)