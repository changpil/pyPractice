"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

"""


def findMaxLength(nums):
    # Track imbalance of #1s - #0s
    hmap = {0:0}
    prefixExcess = 0
    maxsize = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            prefixExcess += 1
        else:
            prefixExcess -= 1

        if prefixExcess in hmap:
            maxsize = max(maxsize, i  + 1 - hmap[prefixExcess])
        if prefixExcess not in hmap:
            hmap[prefixExcess] = i + 1
    return maxsize

# nums = [0,1] # 2
# print(findMaxLength(nums))
#
# nums = [0,1,0] # 2
# print(findMaxLength(nums))

nums = [0,0,0,1,0,0,1] # 4
print(findMaxLength(nums))

nums = [0,1,1,0,1,1,1,0] # 4
print(findMaxLength(nums))