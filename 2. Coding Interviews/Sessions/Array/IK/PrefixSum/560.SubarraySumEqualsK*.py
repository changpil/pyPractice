"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Time complexity O(n)
"""

"""
Array n

0, ----, i-1, i, ... n 
Total # of subarrays adding up to k ending at index i

How many subarrays with sum = k - nums[i] ended at i - 1?
"""
def subarraySum(nums, k):
    sumUptoi = {}
    # This is the case adding up to k [0,...i] = k
    # [1],  k = 0 or [1,1] , k = 2
    sumUptoi[0] = 1
    count = 0
    runningSum =0
    for num in nums:
        runningSum += num
        if runningSum - k in sumUptoi:
            count += sumUptoi[runningSum - k]
        sumUptoi[runningSum] = sumUptoi.get(runningSum, 0) + 1

    return count

nums = [ 5, 5, 5, 1]
print(subarraySum(nums, 1))

nums = [1]
print(subarraySum(nums, 1))




