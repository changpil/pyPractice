"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""


def longestOnes(nums, k):
    i, j, flips = 0, 0, 0
    while j < len(nums) and flips < k:
        if nums[j] == 0:
            flips += 1
        j += 1
    max1 = j

    while j < len(nums):
        if nums[j] == 0:
            flips += 1
        # Error with i < j
        while i <= j and flips > k:
            if nums[i] == 0:
                flips -= 1
            i += 1
        j += 1
        max1 = max(max1, j - i)

    return max1

nums = [1,1,1,0,0,0,1,1,1,1,0]
print(longestOnes(nums, 2))  # 6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(longestOnes(nums, 3)) # 10


# Edge Cases
nums=[0,0,0,0]
print(longestOnes(nums, 0)) # 0