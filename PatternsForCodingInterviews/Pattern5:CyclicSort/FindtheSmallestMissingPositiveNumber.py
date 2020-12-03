# Given an unsorted array containing numbers, find the smallest missing positive number in it.
#
# Example 1:
#
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Example 2:
#
# Input: [3, -2, 0, 1, 2]
# Output: 4
# Example 3:
#
# Input: [3, 2, 5, 1]
# Output: 4

def find_first_missing_positive(nums):
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] <= 0:
            i += 1
        elif j < len(nums) and nums[i] == nums[j]:
            i += 1
        elif nums[i] > len(nums):
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]

    print(nums)
    prev = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            return i + 1
        if nums[i] != prev + 1:
            return i + 1
        prev += 1
    return len(nums)



print(find_first_missing_positive([-3, 1, 5, 4, 2]))
print(find_first_missing_positive([3, -2, 0, 1, 2]))
print(find_first_missing_positive([3, 2, 5, 1]))