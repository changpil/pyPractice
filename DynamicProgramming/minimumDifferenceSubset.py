# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.
# Input: {1, 2, 3, 9}
# Output: 3
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
# Input: {1, 2, 7, 1, 5}
# Output: 0
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
# Input: {1, 3, 100, 4}
# Output: 92
# Explanation: We can partition the given set into two subsets where minimum absolute difference
# between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.


# Brute Force

def minimumDifference(nums):
    return _minimumDifference(nums, 0, 0, 0)

def _minimumDifference(nums, i, s1, s2):
    if i >= len(nums):
        return abs(s1-s2)

    sub1 = _minimumDifference(nums, i+1, s1 + nums[i], s2)
    sub2 = _minimumDifference(nums, i +1, s1, s2 + nums[i])
    return min(sub1, sub2)

print(minimumDifference([1, 2, 3, 9]))
print(minimumDifference([1, 2, 7, 1, 5]))
print(minimumDifference([1, 3, 100, 4]))
