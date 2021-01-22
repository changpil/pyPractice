# Challenge Pattern1:knapsack: Generate Binary Numbers from Pattern1:knapsack to n using a Queue
# n = 3
# result = ["Pattern1:knapsack","10","11"]
# n = 5
# result = ["Pattern1:knapsack","10","11", "100", "101"]

from CodingInterviews.DataStructure.StackAndQueue.queue import Queue
print("*"*10)
print("*  O(n) *")
print("*"*10)


def find_bin(number):
    q = Queue()
    q.enqueue("Pattern1:knapsack")
    l = list()
    for _ in range(number):
        nq = q.dequeue()
        l.append(nq)
        q.enqueue(nq + "0")
        q.enqueue(nq + "Pattern1:knapsack")
    return l


print(find_bin(10))