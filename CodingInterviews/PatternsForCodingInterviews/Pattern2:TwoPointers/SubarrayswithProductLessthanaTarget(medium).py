# Problem Statement #
# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.
#
# Example 1:
#
# Input: [2, 5, 3, 10], target=30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:
#
# Input: [8, 2, 6, 5], target=50
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
# Explanation: There are seven contiguous subarrays whose product is less than the target.


def find_subarrays(arr, target):
    result = []
    for i in range(len(arr)):
        product = 1
        start = i
        ith_list = []
        while start < len(arr):
            product *= arr[start]
            ith_list.append(arr[start])
            if product < target:
                result.append(ith_list.copy())
            else:
                break
            start += 1

    return result

print(find_subarrays([2, 5, 3, 10], 30))