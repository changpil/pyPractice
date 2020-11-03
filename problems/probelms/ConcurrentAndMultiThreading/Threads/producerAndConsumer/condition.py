import threading
counter = 0
def consumer(shared_resource, condition):
    condition.acquire()
    if len(shared_resource) == 0:
        condition.wait()
    item = shared_resource.pop()
    print("consumer: {}".format(item))
    condition.release()

def producer(shared_resource, condition):
    condition.acquire()
    global counter
    shared_resource.append(counter)
    counter += 1
    print("producer: {}".format(counter -1))
    condition.notify()
    condition.release()

shared_resource =list()
condition = threading.Condition()
con_threads, pro_threads = [], []

for i in range(10):
    t = threading.Thread(target=consumer, args=(shared_resource, condition))
    con_threads.append(t)

for i in range(10):
    t = threading.Thread(target=producer, args=(shared_resource, condition))
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