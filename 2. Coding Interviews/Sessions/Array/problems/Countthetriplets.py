"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets:
1 + 2 = 3 and 3 +2 = 5
â€‹Example 2:

Input:
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits
Your Task:
You don't need to read input or print anything. Your task is to complete the function countTriplet() which takes the array arr[] and N as inputs and returns the triplet count

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)
"""


def countTriplet(nums):
    nums.sort()
    count = 0
    for target_i in range(2, len(nums)):
        start , end = 0, target_i -1
        while start < end:
            if nums[start] + nums[end] == nums[target_i]:
                count +=1
                # Wrong
                #break
                start += 1
                end -= 1
            elif nums[start] + nums[end] > nums[target_i]:
                end -= 1
            else:
                start += 1
    return count
nums= [1, 5, 3, 2]
print(countTriplet(nums))
nums = [2, 3, 4]
print(countTriplet(nums))

nums = [3, 6, 8, 11, 14, 16]
print(countTriplet(nums))