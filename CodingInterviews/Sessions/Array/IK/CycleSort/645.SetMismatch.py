"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

Time Complexcity:  O(n)
Space Complexity: O(1)
"""


def findErrorNums(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            d = nums[i] -1
            if nums[d] == d + 1:
                break
            else:
                nums[i], nums[d] = nums[d] , nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return nums[i], i + 1

nums = [1,2,2,4]
print(findErrorNums(nums))
