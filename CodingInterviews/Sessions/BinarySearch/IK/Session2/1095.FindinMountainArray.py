"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.



Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
"""


def findInMountainArray(nums, target):
    start, end = 1, len(nums) -2
    top_i = -1
    while start <= end:
        mid = (start + end) //2
        if nums[mid -1] < nums[mid] > nums[mid +1]:
            top_i = mid
            break
        elif nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            end = mid -1

    start, end = 0, top_i
    while start <= end:
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    start, end = top_i, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            start = mid + 1
        else:
            end = mid -1
    return -1
nums = [1,5,2]
print(findInMountainArray(nums, 2))

nums = [1,2,3,4,5,3,1]
print(findInMountainArray(nums, 3))

nums = [0,1,2,4,2,1]
print(findInMountainArray(nums, 3))

