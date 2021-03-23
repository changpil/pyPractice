"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2
"""

# def peakIndexInMountainArray(nums):
#     start, end = 1 , len(nums) - 2
#     while start <= end:
#         mid = (start + end) //2
#         if nums[mid -1] < nums[mid] > nums[mid +1]:
#             return mid
#         elif nums[mid] < nums[mid +1]:
#             start = mid +1
#         else:
#             end = mid -1
#     return -1

def peakIndexInMountainArray(nums):
    start, end= 0, len(nums)-1
    while start <= end:
        mid = (start + end) //2
        if mid + 1 < len(nums) and nums[mid] <= nums[mid +1]:
            start = mid +1
        else:
            end = mid - 1
    return start

nums = [0,1,0] # 1
print(peakIndexInMountainArray(nums))

nums = [0,2,1,0] # 1
print(peakIndexInMountainArray(nums))

nums = [0,10,5,2] #1
print(peakIndexInMountainArray(nums))

nums = [3,4,5,1] #2
print(peakIndexInMountainArray(nums))

nums = [24,69,100,199,79,78,67,36,26,19] #3
print(peakIndexInMountainArray(nums))