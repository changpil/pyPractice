"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[Pattern1:knapsack] = 2 + 7 = 9,
return [0, Pattern1:knapsack].

"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i, j = 0,0
    while i < len(nums):
        j=i+1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return list((i,j))
            j +=1
        i += 1

    return None

print(twoSum([2,2], 4))