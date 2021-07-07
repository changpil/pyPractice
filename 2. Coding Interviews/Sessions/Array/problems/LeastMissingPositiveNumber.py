"""
We have an unsorted array of integers such as the following:

JAVASCRIPT
[0, 3, -1, -2, 1]
In the above example, the minimum number is -2 and the maximum is 3. If it were sorted, it would look like:

JAVASCRIPT
[-2, -1, 0, 1, 3]
This means there is an expected range (defined as the collection of values between the minimum and maximum values) of [-2, -1, 0, 1, 2, 3] for the array.

But look at the example again:

JAVASCRIPT
[-2, -1, 0, 1, 3]
We're missing a number: 2. The smallest missing positive integer for our input array is 2.


Can you write a method that takes such an array and returns the first missing positive integer?

JAVASCRIPT
leastMissingPositive([1, 2, 3, 0])
// 4
In the above example, it is 4 since we already have 0 through 3. Have your code run in O(n) time with constant space (hence, we can easily determine if it was sorted, but most sorts will take O(n * log n) time).
"""


# def least_missing_pos(nums):
#     if len(nums) == 0:
#         return 1
#     _min = min(nums)
#     if _min > 0:
#         return 1
#
#     delta = -_min
#     i = 0
#     while i < len(nums):
#         while i != nums[i] + delta:
#             targetIndex = nums[i] + delta
#             if targetIndex >= len(nums):
#                 break
#             if targetIndex == nums[targetIndex] + delta:
#                 break
#             nums[i], nums[targetIndex] = nums[targetIndex], nums[i]
#         i += 1
#     print(nums)
#     i = 0
#     while i < len(nums):
#         if i != nums[i] + delta and i + delta > 0:
#             return i + delta
#         i += 1
#     if len(nums) - delta > 0:
#         return len(nums) - delta
#     return 1
#
# nums = [-10,1, 10]
# print(least_missing_pos(nums))

def least_missing_pos(nums):
    if len(nums) == 0:
        return 1
    i = 0
    while i < len(nums):
        while i != nums[i]:
            targetIndex = nums[i]
            if not 0 <= targetIndex < len(nums):
                break
            if targetIndex == nums[targetIndex]:
                break
            nums[i], nums[targetIndex] = nums[targetIndex], nums[i]
        i += 1

    for i in range(len(nums)):
        if i != nums[i] and i > 0:
            return i
    return len(nums)

nums = [-10,1, 10]
print(least_missing_pos(nums))

nums = [-20, -10, -5, -1 ]
print(least_missing_pos(nums))

nums = [20, 10, 5, 7 ]
print(least_missing_pos(nums))

nums = [-1, 0, 2, 1 ]
print(least_missing_pos(nums))