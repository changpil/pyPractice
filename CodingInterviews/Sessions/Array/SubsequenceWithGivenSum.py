"""
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def subSequenceSum(nums,s):
    start, end = 0, 0
    tmpSum = 0
    while end < len(nums):
        tmpSum += nums[end]
        while start <= end and tmpSum > s:
            tmpSum -= nums[start]
            start += 1
        if tmpSum == s:
            return start+1, end +1
        end += 1
    return -1


a = [1, 2, 3, 7, 5]
print(subSequenceSum(a, 12))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(subSequenceSum(a, 15))