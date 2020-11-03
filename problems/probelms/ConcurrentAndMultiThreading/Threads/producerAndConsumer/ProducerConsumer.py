import queue, threading , time

#producer Consumer with queue.Queue()
def worker():

    while True:
        item = q.get()
        if item is None:
            break
        print(item)
        time.sleep(2)
        q.task_done()

    #If there is no while loop, then the thread can tap one from queue then thread is done.
    """
    item = q.get()
    print(item)
    time.sleep(2)
    q.task_done()
    """

q = queue.Queue()
threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in range(30):
    q.put(item)

# block until all tasks are done
#q.join()

print("enf of q.join")
# stop workers
for i in range(10):
    q.put(None)

#print("enf of q.put(None)")
#for t in threads:
#    t.join()

print("end of main"*30)