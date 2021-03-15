"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

def findPeakElement(nums):

    start, end= 0, len(nums)-1
    while start <= end:
        mid = (start + end) //2
        if mid + 1 < len(nums) and nums[mid] <= nums[mid +1]:
            start = mid +1
        else:
            end = mid - 1
    return start


nums = [1,2,3,1]
print(findPeakElement(nums))
nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))
nums = [1] # expected 0
print(findPeakElement(nums))

nums = [1, 2] # expected 1
print(findPeakElement(nums))
nums = [2, 1] # expected 0
print(findPeakElement(nums))

nums = [1, 2, 3] # expected 1
print(findPeakElement(nums))
nums = [3, 2, 1] # expected 0
print(findPeakElement(nums))

# Facebook Phone interview
def findLocalMinmumElement(nums):

    start, end= 0, len(nums)-1
    while start <= end:
        mid = (start + end) //2
        if mid + 1 < len(nums) and nums[mid] < nums[mid +1]:
            end = mid - 1
        else:
            start = mid + 1
    if start == len(nums):
        return end
    return start

print("Facebook Phone interview: findLocalMinmumElement")
nums = [1,2,3,1] # epected 0 0r 3
print(findLocalMinmumElement(nums))
nums = [1,2,1,3,5,6,4] # expected 0 or 2
print(findLocalMinmumElement(nums))
nums = [1] # expected 0
print(findLocalMinmumElement(nums))
nums = [1, 2] # expected 0
print(findLocalMinmumElement(nums))
nums = [2, 1] # expected 1
print(findLocalMinmumElement(nums))
nums = [1, 2, 3] # expected 0
print(findLocalMinmumElement(nums))
nums = [3, 2, 1] # expected 2
print(findLocalMinmumElement(nums))