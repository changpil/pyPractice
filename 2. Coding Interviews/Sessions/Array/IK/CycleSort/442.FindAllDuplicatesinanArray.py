"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

Time Complexcity:  O(n)
Space Complexity: O(1)
"""

def findDuplicates(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            d = nums[i] - 1
            if nums[d] == d + 1:
                break
            else:
                nums[d], nums[i] = nums[i], nums[d]
    result = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            result.append(nums[i])
    return result

nums = [1,1,3,3,2,2]
print(findDuplicates(nums))

nums = [4, 5, 1,1,3,3,2,2]
print(findDuplicates(nums))