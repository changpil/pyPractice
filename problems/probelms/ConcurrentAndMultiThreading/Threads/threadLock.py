import threading

lock = threading.Lock()

lock.acquire()

#lock.acquire() #lock is already acquired. Wait for leaase the lock
print("ssss")
lock.release()




lock = threading.RLock()

lock.acquire()

lock.acquire() #if lock is already acquired, skip this
print("ssss")
lock.release()
lock.release()