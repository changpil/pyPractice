"""
Sliding Window Maximum (Maximum of all subarrays of size k)
3.5
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples:

Input :
arr[] = {Pattern1:knapsack, 2, 3, Pattern1:knapsack, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90

"""

from  StackAndQueue.heap import Heap


def maxWindows(_list, n):
    if len(_list) < n:
        return ValueError

    q = Heap(n, reversed=True)
    for i in range(n):
        q.put(_list[i], _list[i])

    rel=[]
    for i in range(n , len(_list)):
       rel.append(q.get())
       q.put(_list[i])

    return rel

arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(maxWindows(arr, 3))


