"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""

def wiggleSort(nums):
    greater = True

    for i in range(1, len(nums)):
        if greater:
            if nums[i-1] <= nums[i]:
                pass
            else:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        else:
            if nums[i-1] >= nums[i]:
                pass
            else:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        greater = not greater

    return nums

nums = [3,5,2,1,6,4]
print(wiggleSort(nums))

nums = [1,2,3,4,5,6]
print(wiggleSort(nums))

nums = [6,5,4,3,2,1]
print(wiggleSort(nums))