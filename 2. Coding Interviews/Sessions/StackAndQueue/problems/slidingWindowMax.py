"""
Pattern1: SlidingWindow Maximum (Maximum of all subarrays of size k)
3.5
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

Examples:

Input :
arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}
k = 3
Output :
3 3 4 5 5 5 6

Input :
arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}
k = 4
Output :
10 10 10 15 15 90 90

"""


def maxWindows(l, windows):
    heap = []
    for i in range(windows):
        heap.append(l[i])
    maxValues = []
    for i in range(windows, len(l)):
        maxValues.append(max(heap))
        heap.remove(l[i-windows])
        heap.append(l[i])
    maxValues.append(max(heap))
    return maxValues



arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
print(maxWindows(arr, 3)) # 3 3 4 5 5 5 6

arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
print(maxWindows(arr, 4)) # 10 10 10 15 15 90 90