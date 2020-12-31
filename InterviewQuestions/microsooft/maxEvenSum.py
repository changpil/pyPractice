# Find the max even sum from an array

from heapq import *
def maxEvenSum(arr, k):
    visited = set()
    sums, runningSum = [], []
    helper(arr, k, visited, sums, runningSum)

    sums = list(map(lambda a: a*-1, sums))
    heapify(sums)

    while sums:
        c = -heappop(sums)
        if c%2 == 0:
            return c
    return -1

def helper(arr, k, visited, sums, runningSum):
    if k == 0:
        sums.append(sum(runningSum))
        return

    for i in range(len(arr)):
        if i not in visited:
            visited.add(i)
            runningSum.append(arr[i])
            helper(arr, k-1, visited, sums, runningSum)
            runningSum.pop()
            visited.remove(i)


print(maxEvenSum([4, 9, 8, 2, 6], 3))
print(maxEvenSum([5, 6, 3, 4, 2], 3))
print(maxEvenSum([7,7,7,7], 1))



# Appreciate that you will do one of two things with the total sum of all elements in the array. If the total sum be even, you return that number, but if it be odd, then you will have to remove a number in order to make it even. Note that removing an even number will leave the remaining sum odd, so there is no point in removing an even number. But, since the total sum be odd, then there must be at least one odd number in the array.
#
# So all you need to do if the total sum be odd is to iterate over the array and remove the smallest odd number. And there is guaranteed to be at least one odd number.