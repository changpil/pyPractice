"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""
# My first Implementation
# I did not understand the clear logic.
# def maxSubArray(l):
#     _max = l[0]
#     candidate = l[0]
#
#     for i in range(1, len(l)):
#         if _max < 0 and l[i] <= 0:
#             _max = max(l[i], _max)
#         elif _max > 0 and l[i] <= 0:
#             candidate = candidate + l[i]
#         elif i > 0 and l[i-1] < 0:
#             _max = max(_max , _max + candidate, l[i])
#         else:
#             _max = max(_max + l[i], _max + candidate, l[i])
#     return _max

# Brute Force O(n^3)
# for i in range(len(nums)):
#     for j in rnage(i + 1, len(nums)):
#         sum(nums[i:j])

# Brute Force O(n^2)
# globalmax
# for i in range(len(nums)):
#     imax = 0
#     for j in range(i, len(nums)):
#         imax += nums[j]
#      globalmax = max(globalmax, imax)

def maxSubArray(nums):
    globalmax = nums[0]
    continuousmax = nums[0]
    for i in range(1, len(nums)):
        continuousmax = max(continuousmax + nums[i], nums[i])
        globalmax = max(globalmax, continuousmax)
    return globalmax

nums = [-1,-2,-3,-4,-5]
print(maxSubArray(nums))
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
nums = [5,4,-1,7,8]
print(maxSubArray(nums))