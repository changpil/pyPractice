"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""
# Not working nums = [2,3,4,5,1]
# def findMin(nums):
#     start , end = 0, len(nums) -1
#     while start <= end:
#         mid = (start + end) //2
#         if mid + 1 < len(nums) and nums[mid] < nums[mid +1]:
#             end = mid -1
#         else:
#             start = mid + 1
#     if start == len(nums):
#         return nums[end]
#     return nums[start]
# Not working  nums=[4,5,1,2,3]
def findMin(nums):
    start , end = 0, len(nums) -1
    while start <= end:
        mid = (start + end) //2
        if nums[mid] > nums[-1]:
            start = mid + 1
        else:
            end = mid - 1
    # if start +1 <len(nums) and nums[start] > nums[start +1]:
    #     return nums[start +1]
    return nums[start]

nums = [1,2,3]
print(findMin(nums))
nums = [3, 1, 2]
print(findMin(nums))
nums = [3, 2, 1]
print(findMin(nums))
nums = [3,4,5,1,2]
print(findMin(nums))
nums = [4,5,6,7,0,1,2]
print(findMin(nums))
nums = [11,13,15,17]
print(findMin(nums))
nums = [2,3,4,5,1]
print(findMin(nums))
nums=[4,5,1,2,3]
print(findMin(nums))


def findMinIndexWithDuplicates(nums):
    start , end = 0, len(nums) -1
    while nums[start] == nums[-1]:
        start += 1
    while start <= end:
        mid = (start + end) //2
        if nums[mid] > nums[-1]:
            start = mid + 1
        else:
            end = mid - 1
    return start

print("findMinIndexWithDuplicates")
# nums = [1,2,3]
# print(findMinIndexWithDuplicates(nums))
# nums = [3, 1, 2]
# print(findMinIndexWithDuplicates(nums))
# nums = [3, 2, 1]
# print(findMinIndexWithDuplicates(nums))
# nums = [3,4,5,1,2]
# print(findMinIndexWithDuplicates(nums))
# nums = [4,5,6,7,0,1,2]
# print(findMinIndexWithDuplicates(nums))
# nums = [11,13,15,17]
# print(findMinIndexWithDuplicates(nums))
# nums = [2,3,4,5,1]
# print(findMinIndexWithDuplicates(nums))
# nums=[4,5,1,2,3]
# print(findMinIndexWithDuplicates(nums))

nums = [1,1, 2,3]
print(findMinIndexWithDuplicates(nums))
nums = [3, 1, 1, 1,  2, 2]
print(findMinIndexWithDuplicates(nums))
nums = [3, 2, 1, 1, 1, 1, 1]
print(findMinIndexWithDuplicates(nums))
nums = [1,0,1,1,1]
print(findMinIndexWithDuplicates(nums))
nums = [1,1,1,1,1,0,1,1]
print(findMinIndexWithDuplicates(nums))
# nums = [11,13,15,17]
# print(findMinIndexWithDuplicates(nums))
# nums = [2,3,4,5,1]
# print(findMinIndexWithDuplicates(nums))
# nums=[4,5,1,2,3]
# print(findMinIndexWithDuplicates(nums))