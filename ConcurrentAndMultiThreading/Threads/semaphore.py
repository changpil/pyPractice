import threading

#This is same as threading.Lock()
"""
semaphore = threading.Semaphore()

semaphore.acquire()
semaphore.acquire()
print("SSSSS")
semaphore.release()
semaphore.release()
"""

#in normal semaphore, if you call more than dedicated number, this can be a deadlock

semaphore = threading.Semaphore(2)

semaphore.acquire()
semaphore.acquire()
print("SSSSS")
semaphore.release()
semaphore.release()
semaphore.release()
semaphore.release()

semaphore.acquire()
semaphore.acquire()
semaphore.acquire()
print("DDDDD")
semaphore.release()
semaphore.release()
semaphore.release()
"""
Creates a new semaphore. value is the initial value for the counter. 
If value is omitted, the counter is set to a value of knapsack.A BoundedSemaphore works exactly like a Semaphore 
except the number of release() operations cannot exceed the number of acquire() operations.
"""
semaphore = threading.BoundedSemaphore(2)

semaphore.acquire()
semaphore.acquire()

print("SSSSS")
semaphore.release()
semaphore.release()
semaphore.release()