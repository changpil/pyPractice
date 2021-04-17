"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.


Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1


Time Complexcity:  O(n)
Space Complexity: O(1)
"""


def findDuplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            d = nums[i] - 1
            if nums[d] == d + 1:
                break
            else:
                nums[d], nums[i] = nums[i], nums[d]
    result = []
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(nums[i])
    return result

# nums = [1,3,4,2,2]
# print(findDuplicate(nums))
#
# nums = [1,3,3,2,2]
# print(findDuplicate(nums))
#
#
# nums = [1,1,3,3,2,2]
# print(findDuplicate(nums))
#
# nums = [4, 5, 1,1,3,3,2,2]
# print(findDuplicate(nums))

#out Of index
# nums = [4, 5, 1,1,3,3,2, 2, 2, 4,12]
# print(findDuplicate(nums))

nums = [4, 5, 1,1,3,3,2, 2, 2, 4,11]
print(findDuplicate(nums))
