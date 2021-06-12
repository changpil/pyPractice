import time
class Bank:
    def __init__(self):
        self.bal = 0

    def deposit(self, amt):
        balance = self.bal
        time.sleep(0.1)
        self.bal = balance + amt

    def withdraw(self, amt):
        balance = self.bal
        time.sleep(0.1)
        self.bal = balance -amt

import threading
b = Bank()

deposit = threading.Thread(target=b.deposit, args=(1,))
withdraw = threading.Thread(target=b.withdraw, args=(1,))

#withdraw.start()
deposit.start()
withdraw.start()

deposit.join()
withdraw.join()
print(b.bal)

print("#"*30)
class BankWithLock:
    def __init__(self):
        self.bal = 0
        self.lock = threading.Lock()

    def deposit(self, amt):
        with self.lock:
            #self.lock.acquire()
            balance = self.bal
            time.sleep(0.1)
            self.bal = balance + amt
            #self.lock.release()

    def withdraw(self, amt):
        with self.lock:
            #self.lock.acquire()
            balance = self.bal
            time.sleep(0.1)
            self.bal = balance -amt
            #self.lock.release()

b = BankWithLock()

deposit = threading.Thread(target=b.deposit, args=(1,))
withdraw = threading.Thread(target=b.withdraw, args=(1,))

#withdraw.start()
deposit.start()
withdraw.start()

deposit.join()
withdraw.join()
print(b.bal)
