"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Time Complexcity:  O(n)
Space Complexity: O(1)
"""

def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        while nums[i] != i:
            d = nums[i]
            if nums[d] == d:
                break
            else:
                nums[d], nums[i] = nums[i], nums[d]
    result = []
    for i in range(len(nums)):
        if nums[i] != i:
            result.append(i)

    return result

nums = [2,2,2]
print(findDisappearedNumbers(nums))