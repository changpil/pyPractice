import threading, time

class BankAccount:
    def __init__(self):
        self.bal = 0
        self.lock = threading.Lock()
    def deposit(self, amt):
        with self.lock:
            #DEADLOCK
            #self.lock.acquire()
            balance = self.bal
            time.sleep(2)
            self.bal = balance + amt
            #self.lock.release()

    def withdraw(self, amt):
        with self.lock:
            balance = self.bal
            if balance - amt < 0:
                raise Exception("Not enoug balance: {}".format(self.bal))
            time.sleep(2)
            self.bal = balance - amt

b = BankAccount()
t1 = threading.Thread(target= b.deposit, args =(100,))
t2 = threading.Thread(target= b.withdraw, args =(50,))

t1.start()
t2.start()
t1.join()
t2.join()

print(b.bal)
