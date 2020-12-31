# Given an array arr[] of N positive elements, the task is to find a pair in the array such that the digit sum of elements in the pair are equal and their sum is maximum.
# Print -1 if it is not possible to find the pair else print the maximum sum.

def getKey(num):
    key = 0
    while num:
        num, rm = divmod(num, 10)
        key += rm
    return key

from heapq import *
import math
def maxSumOfTwoElements(nums):
    d = {}
    for num in nums:
        q = d.get(getKey(num), [])
        if len(q) == 2:
            if q[0] < num:
                heappop(q)
                heappush(q, num)
        else:
            heappush(q, num)
        d[getKey(num)] = q

    maxTwoEle = -1
    for q in d.values():
        if len(q) == 2:
            maxTwoEle = max(maxTwoEle, sum(q))
    return maxTwoEle

print(maxSumOfTwoElements([71, 23,32, 131, 17]))
