"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""

# def findMaxAverage(nums, k):
#     start, end = 0, k
#     globalMax = runningSum = sum(nums[:k])
#     while end < len(nums):
#         runningSum = runningSum - nums[start] + nums[end]
#         start += 1
#         end += 1
#     return globalMax/k


def findMaxAverage(nums, k):
    globalMax = windowSum = sum(nums[:k])
    for i in range(k, len(nums)):
        windowSum += nums[i] - nums[i-k]
        globalMax = max(globalMax, windowSum)
    return globalMax/k


nums = [1,12,-5,-6,50,3]

print(findMaxAverage(nums, 4))
