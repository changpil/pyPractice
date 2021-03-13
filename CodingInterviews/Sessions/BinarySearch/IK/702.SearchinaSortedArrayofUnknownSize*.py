"""
Given an integer array sorted in ascending order, write a function to search target in nums.
If target exists, then return its index, otherwise return -1. However, the array size is unknown to you.
You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.
"""

"""
NOTE:
You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
The length of the array will be in the range [1, 10^4].
"""


"""
This is ArrayReader's API interface.
You should not implement it, or speculate about its implementation
"""
class ArrayReader(object):
    def __init__(self, nums):
        self.nums = nums
    def get(self, index):
        if not (0 <= index < len(self.nums)):
            return 2147483647
        return self.nums[index]

# def getStartEnd(reader, target):
#     start, end  = 0, 2
#     while not (reader.get(start) <= target <= reader.get(end)):
#         start = end
#         end *= end
#         if reader.get(start) == 2147483647:
#            return 1, -1
#     return start, end

def search(reader, target):
    #start, end = getStartEnd(reader, target)
    end = 1
    while reader.get(end) <= target:
        end *= 2
    start = end//2
    while start <= end:
        mid = (start + end) // 2
        res = reader.get(mid)
        if res == target:
            return mid
        elif res < target:
            start = mid + 1
        elif res > target:
            end = mid - 1
    return -1

a = [i for i in range(1000)]
reader = ArrayReader(a)
print(search(reader, -1))
print(search(reader, 0))
print(search(reader, 999))
print(search(reader, 1000))