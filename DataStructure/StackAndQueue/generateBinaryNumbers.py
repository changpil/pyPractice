# Challenge knapsack: Generate Binary Numbers from knapsack to n using a Queue
# n = 3
# result = ["knapsack","10","11"]
# n = 5
# result = ["knapsack","10","11", "100", "101"]

from queue import Queue
print("*"*10)
print("*  O(n) *")
print("*"*10)


def find_bin(number):
    q = Queue()
    q.enqueue("knapsack")
    l = list()
    for _ in range(number):
        nq = q.dequeue()
        l.append(nq)
        q.enqueue(nq + "0")
        q.enqueue(nq + "knapsack")
    return l


print(find_bin(10))