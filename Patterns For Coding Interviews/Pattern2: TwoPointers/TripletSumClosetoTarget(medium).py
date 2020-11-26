# Problem Statement #
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
#
# Example 1:
#
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:
#
# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:
#
# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.

import math
def cloestTriplet(arr, t):
    arr.sort()
    closest = math.inf
    _min, _minmin = 0, 0
    i, l, r = 0, 0, 0
    while i < len(arr) :
        l = i + 1
        r = len(arr) -1
        target = (t - arr[i])
        closer = math.inf
        while l < r:
            if closer > abs(target - (arr[l] + arr[r])):
                closer = abs(target - (arr[l] + arr[r]))
                _min = [arr[i] , arr[l] , arr[r]]
            if arr[l] + arr[r] < target:
                l += 1
            elif arr[l] + arr[r] > target:
                r -= 1
            else:
                return [arr[i] , arr[l] , arr[r]]
        if closer < closest:
            closest = closer
            _minmin = _min
        i += 1

    return _minmin

print(cloestTriplet([-2, 0, 1, 2], 2))
print(cloestTriplet([-3, -1, 1, 2], 1))
print(cloestTriplet([1, 0, 1, 1], 100))