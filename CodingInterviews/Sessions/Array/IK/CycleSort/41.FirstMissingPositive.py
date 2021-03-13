"""
Given an unsorted integer array nums, find the smallest missing positive integer.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

Time Complexcity:  O(n)
Space Complexity: O(1)
"""

def firstMissingPositive(nums):
    #   0 <= index < len(nums)
    #   1 <= value < 1 + len(nums)
    # nums[0] = 1
    # nums[1] = 2
    if nums == None or len(nums) == 0:
        return 1

    for i in range(len(nums)):
        while nums[i] != i + 1:
            d = nums[i] - 1
            if d < 0 or d >= len(nums) or nums[d] == d + 1:
                break
            else:
                nums[i], nums[d] = nums[d], nums[i]
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1

nums = [1,2,0]
print(firstMissingPositive(nums))

nums = [3,4,-1,1]
print(firstMissingPositive(nums))

nums = [-1]
print(firstMissingPositive(nums))

nums = [1]
print(firstMissingPositive(nums))
nums = [1, 1]
print(firstMissingPositive(nums))