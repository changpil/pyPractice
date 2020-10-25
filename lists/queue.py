class Queue:
    def __init__(self):
        self.q = list()
    def put(self, item):
        self.q.insert(0, item)
    def get(self):
        return self.q.pop()

q = Queue()
for i in range(5):
    q.put(i)

for _ in range(5):
    print(q.get())

'''
# python queue are synchronous queue
import threading, queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')
'''