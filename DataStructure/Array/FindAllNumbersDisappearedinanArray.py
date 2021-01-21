# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

# My Solution O(n)
# n  + 1, 1, 1, 1 = n +(n-1) = O(2n -1)
# def findDisappearedNumbers(self, nums):
#     i = 0
#     a = nums
#     while i < len(nums):
#         while a[i] != i + 1:
#             if a[a[i] - 1] == a[i]:
#                 break
#             a[a[i] - 1], a[i] = a[i], a[a[i] - 1]
#         i += 1
#
#     returnList = []
#     for i in range(len(nums)):
#         if a[i] != i + 1:
#             returnList.append(i + 1)
#     return returnList

def findDisappearedNumbers(self, nums):
    s = set()


    returnList = []
    for i in range(len(nums)):
        if a[i] != i + 1:
            returnList.append(i + 1)
    return returnList