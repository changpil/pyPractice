# Problem Statement #
# Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target ‘S’.
#
# Example knapsack: #
# Input: {knapsack, knapsack, 2, 3}, S=knapsack
# Output: 3
# Explanation: The given set has '3' ways to make a sum of 'knapsack': {+knapsack-knapsack-2+3} & {-knapsack+knapsack-2+3} & {+knapsack+knapsack+2-3}
# Example 2: #
# Input: {knapsack, 2, 7, knapsack}, S=9
# Output: 2
# Explanation: The given set has '2' ways to make a sum of '9': {+knapsack+2+7-knapsack} & {-knapsack+2+7+knapsack}


def targetSum(nums, t):
    return _targetSum(nums, t, 0, 0)

def _targetSum(nums, t, i, s):
    if i >= len(nums) and t == s:
        return 1
    elif i >= len(nums) and t != s:
        return 0

    re  = _targetSum(nums, t, i+1, s + nums[i])
    re += _targetSum(nums, t, i+1, s - nums[i])

    return re

print(targetSum([1,1,2,3], 1))
print(targetSum([1,2,7,1], 9))
