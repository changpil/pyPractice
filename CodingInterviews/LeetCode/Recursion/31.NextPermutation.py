#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order(i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.
#
# Example1:
# Input: nums = [1, 2, 3]
# Output: [1, 3, 2]

# Example2:
# Input: nums = [3, 2, 1]
# Output: [1, 2, 3]

# Example3:
# Input: nums = [1, 1, 5]
# Output: [1, 5, 1]

# Example4:
# Input: nums = [1]
# Output: [1]

# Wrong
def nextPermutation(nums):
    stop = False

    for i in range(len(nums)-1, 0, -1):
        if nums[i-1] < nums[i]:
            stop = True
        nums[i - 1], nums[i] = nums[i], nums[i - 1]

        if stop :
             break

    if not stop:
        nums.sort()
    return nums



nums = [1, 2, 3]
print(nextPermutation(nums))
nums = [3, 2, 1]
print(nextPermutation(nums))
nums = [1, 1, 5]
print(nextPermutation(nums))
nums = [1]
print(nextPermutation(nums))


# [3,1,2]
nums = [2,3,1]
print(nextPermutation(nums))