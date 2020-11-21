# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

def maxSubarray(nums, k):
    if len(nums) < k:
        return

    l, r = 0, 0
    s = 0
    while r < k:
        s += nums[r]
        r += 1

    maxmax = s
    while r <len(nums):
        s -= nums[l]
        l += 1
        s += nums[r]
        r += 1
        maxmax = max(maxmax, s)

    return maxmax




print(maxSubarray([2, 1, 5, 1, 3, 2], 3))
print(maxSubarray([2, 3, 4, 1, 5], 2))