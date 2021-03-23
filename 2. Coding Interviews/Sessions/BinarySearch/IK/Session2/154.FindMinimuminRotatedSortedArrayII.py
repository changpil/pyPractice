"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.



Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
"""

def findMin(nums):
    start, end = 0, len(nums) -1
    while nums[start] == nums[-1]:
        start += 1
    # for i in range(len(nums)):
    #     if nums[i] != nums[-1]:
    #         start = i
    #         break
    while start <= end:
        mid = (start + end)//2
        if nums[mid] > nums[-1]:
            start = mid + 1
        else:
            end = mid - 1
    # if start == len(nums):
    #     return nums[end]
    return nums[start]

nums = [1,3,5]
print(findMin(nums))

nums = [2,2,2,0,0, 1]
print(findMin(nums))

nums = [3,1,3]
print(findMin(nums))

nums = [1,3,3]
print(findMin(nums))
