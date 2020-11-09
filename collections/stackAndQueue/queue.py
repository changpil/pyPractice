class Queue:
    def __init__(self):
        self.q = list()
    def enqueue(self, item):
        self.q.insert(0, item)
    def dequeue(self):
        return self.q.pop()
    def front(self):
        return self.q[-1]
    def back(self):
        return self.q[0]
    def isEmpty(self):
        return True if len(self.q) == 0 else False
    def size(self):
        return len(self.s)
    def __str__(self):
        s = ("-"*7 + " queue " + "-"*7 + "\n")
        for i in range(len(self.q)):
            s += f" --> {self.q[i]}"
        s += "\n" + "-" * 20 + "\n"
        return s
# q = Queue()
# for i in range(5):
#     q.enqueue(i)
#
# for _ in range(5):
#     print(q.dequeue())

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