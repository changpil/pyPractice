# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
#
# Example 1:
#
# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
# Example 2:
#
# Input: [2, 3, 4], k=3
# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.
# Example 3:
#
# Input: [-2, -3, 4], k=2
# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.

import math
def find_positive_min_num(nums):
    minnum = math.inf
    for num in nums:
        if num > 0:
            minnum = min(minnum, num)
    return minnum

def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    minnum = find_positive_min_num(nums)
    i = 0
    while i < len(nums):
        j = nums[i] - minnum
        if not 0 <= j < len(nums):
            i += 1
        elif nums[j] == nums[i]:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    #print(nums)
    start = 1
    index = 0

    while k > 0:
        if start < minnum:
            missingNumbers.append(start)
            start += 1
            k -= 1
        else:
            if index < len(nums):
                if nums[index] != start:
                    missingNumbers.append(start)
                    index += 1
                    start += 1
                    k -= 1
                else:
                    # Exist
                    index += 1
                    start += 1
            else:
                missingNumbers.append(start)
                start += 1
                k -= 1
    return missingNumbers

print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
print(find_first_k_missing_positive([2, 3, 4], 3))
print(find_first_k_missing_positive([-2, -3, 4], 2))
