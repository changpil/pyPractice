"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

"""
# My first attempt
# def validMountainArray(nums):
#     if len(nums) < 2:
#         return False
#     up = True
#     fulfilledUp = False
#     fulfilledDown = False
#     for i in range(1, len(nums)):
#         if nums[i - 1] == nums[i]:
#             return False
#         if up:
#             if fulfilledUp and nums[i-1] > nums[i]:
#                 up = not up
#             elif not fulfilledUp and nums[i-1] > nums[i]:
#                 return False
#             elif not fulfilledUp and nums[i-1] < nums[i]:
#                 fulfilledUp = True
#         else:
#             if nums[i-1] > nums[i]:
#                 fulfilledDown = True
#             else:
#                 return False
#     if not fulfilledDown:
#         return False
#     return True

# Two-pointer
def validMountainArray(nums):
    start, end = 0 , len(nums) -1
    if len(nums) < 3:
        return False
    while start + 1 < len(nums) and nums[start] < nums[start + 1]:
        start += 1
    # if start == len(nums) -1 and nums[start-1] < nums[start]:
    #     return False

    while end -1 >= 0 and nums[end-1] > nums[end]:
        end -= 1
    # if end == 0 and nums[end] > nums[end + 1]:
    #     return False

    # if start == end:
    #     return True
    # return False
    return start == end and (0 < start < len(nums)-1)

nums = [2,1]
print(validMountainArray(nums))

nums = [3,5,7, 9]
print(validMountainArray(nums))

nums = [-3,-5,-7, -9]
print(validMountainArray(nums))

nums = [3,5,5]
print(validMountainArray(nums))

nums = [0,3,2,1]
print(validMountainArray(nums))