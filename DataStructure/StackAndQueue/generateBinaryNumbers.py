# Challenge 1: Generate Binary Numbers from 1 to n using a Queue
# n = 3
# result = ["1","10","11"]
# n = 5
# result = ["1","10","11", "100", "101"]

from queue import Queue
print("*"*10)
print("*  O(n) *")
print("*"*10)


def find_bin(number):
    q = Queue()
    q.enqueue("1")
    l = list()
    for _ in range(number):
        nq = q.dequeue()
        l.append(nq)
        q.enqueue(nq + "0")
        q.enqueue(nq + "1")
    return l


print(find_bin(10))