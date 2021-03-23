"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
def search(nums, target):
    start, end = 0, len(nums) -1
    while start <= end:
        mid = (start + end)//2
        if nums[mid] > nums[-1]:
            start = mid + 1
        else:
            end = mid -1
    bottom = start
    # print(bottom)
    if nums[-1] >= target:
        start, end = bottom, len(nums) - 1
    else:
        start, end = 0, bottom - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


nums = [4,5,6,7,0,1,2]
print(search(nums, 0))

nums = [4,5,6,7,0,1,2]
print(search(nums, 3))

nums= [1]
print(search(nums, 1))

nums= [3,5,1]
print(search(nums, 5))