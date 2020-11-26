# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
#
# Example 1:
#
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:
#
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

import math

def longest1(nums, k):
    forgiveness = k
    start, _max = 0,-math.inf

    for i in range(len(nums)):
        if nums[i] == 0:
            forgiveness -= 1
        while forgiveness < 0:
            while nums[start] == 1:
                start += 1
            start += 1
            forgiveness += 1
            # start should be the follwoing 1 to calculate valid bits
            # while start < len(nums) and nums[start] == 1:
            #     start += 1
        _max = max(_max, i - start +1 )

    return _max

#6
print(longest1([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
# 9
print(longest1([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))