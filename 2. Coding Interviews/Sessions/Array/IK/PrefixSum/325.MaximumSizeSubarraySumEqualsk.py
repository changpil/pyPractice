"""
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.



Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""


def maxSubArrayLen(nums, k):
    hmap = {}
    hmap[0] = 0
    prefixSum = 0
    maxSize = 0
    for i, num in enumerate(nums):
        prefixSum += num
        if prefixSum - k in hmap:
            maxSize = max(maxSize, i + 1 - hmap[prefixSum -k])
        if prefixSum not in hmap:
            hmap[prefixSum] = i + 1
    return maxSize

nums = [1,-1,5,-2,3]
print(maxSubArrayLen(nums, 3))

nums = [-2,-1,2,1]
print(maxSubArrayLen(nums, 1))

nums = [2, 2, 0, -2, 0, 0, 2, 0]
print(maxSubArrayLen(nums, 2))

nums = [2, 2, 0, -2, 0, 0, 2, 0]
print(maxSubArrayLen(nums, 1))