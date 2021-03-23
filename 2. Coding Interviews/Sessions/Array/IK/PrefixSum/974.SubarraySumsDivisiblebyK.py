"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""
def subarraysDivByK(nums, k):
    hmap = {}
    hmap[0] = 1
    runningSum = 0
    count = 0
    for num in nums:
        runningSum = (runningSum + num) % k
        if runningSum in hmap:
            count += hmap[runningSum]
        hmap[runningSum] = hmap.get(runningSum, 0) + 1
    return count

nums = [4,5,0,-2,-3,1]
print(subarraysDivByK(nums, 5))