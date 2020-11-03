import threading, time

chapstic = []
for i in range(5):
    chapstic.append(threading.Lock())

class DiningPhilosopher(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.name = i

    def think(self):
        print(str(self.name), " think")
        time.sleep(5)

    def eat(self):
        print(str(self.name), " eat")
        time.sleep(5)

    def pickup(self):
        print(str(self.name), " try to pickup")
        global chapstic
        chapstic[int(self.name)].acquire()
        chapstic[int(self.name)%4 + 1].acquire()
        print(str(self.name), " pickup")
        time.sleep(1)

    def drop(self):
        global chapstic
        chapstic[int(self.name)].release()
        chapstic[int(self.name)%4 +1].release()
        print(str(self.name), " drop")
        time.sleep(1)

    def do(self):
        while True:
            self.think()
            self.pickup()
            self.eat()
            self.drop()

    def run(self):
        self.do()

threads = []
for i in range(5):
    threads.append(DiningPhilosopher(i))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("END")
