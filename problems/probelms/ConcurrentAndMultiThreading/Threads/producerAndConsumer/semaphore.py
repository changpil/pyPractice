import threading
counter = 0

#Wrong solution

def consumer(semaphore, shared_resource):
    while len(shared_resource) == 0:  # need to be critical section
        pass
    semaphore.acquire()
    item = shared_resource.pop()
    print("consumer: {}".format(item))
    semaphore.release()

def producer(semaphore,shared_resource):
    while len(shared_resource) == 5:   # need to be critical section
        pass
    semaphore.acquire()
    global counter
    shared_resource.append(counter)
    counter += 1
    print("producer: {}".format(counter -1))
    semaphore.release()


shared_resource =list()
semaphore = threading.Semaphore(1)

con_threads, pro_threads = [], []

for i in range(10):
    t = threading.Thread(target=consumer, args=(semaphore,shared_resource))
    con_threads.append(t)

for i in range(10):
    t = threading.Thread(target=producer, args=(semaphore,shared_resource))
    pro_threads.append(t)

for t in con_threads:
    t.start()

for t in pro_threads:
    t.start()


for t in con_threads:
    t.join()

for t in pro_threads:
    t.join()


print("end of main")

