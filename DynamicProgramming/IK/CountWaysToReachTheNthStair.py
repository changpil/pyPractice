# Count ways to reach the n'th stair
#
# There are n stairs, a person standing at the bottom wants to reach the top. He can climb a certain number of steps at once.
# For instance, the person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
# Solve the problem for the general case i.e. for n stairs, and different kinds of steps that can be taken (e.g. instead of only 1 or 2 steps, it could be 2, 3 and 5 steps at a time).
#
# Example One
# Input: n=1, steps=[1, 2]
# Output: 1
# Only one way to reach: [{1}]
#
# Example Two
# Input: n=2, steps=[1, 2]
# Output: 2
# Two ways to reach: [{1, 1}, {2}]
#
# Example Three
# Input: n=7, steps=[2, 3]
# Output: 3
# Three ways to reach: [{2, 2, 3}, {2, 3, 2}, {3, 2, 2}]
# Notes
# Input Parameters: There will be two arguments: steps and n.
# An array of distinct integers steps of size m denotes the steps the person can climb at a time and an integer n denotes the total number of stairs to be climbed. The answer is guaranteed to fit in a long integer.
# Output: Return the number of ways to reach the last staircase.


def countWaysToClimb(steps, n):
    DP = [0]*(n+1)
    DP[0] = 1
    for i in range(1, n + 1):
        result = 0
        for k in steps:
            if i - k > 0:
                result += DP[i -k]
            elif i - k == 0:
                result += 1
        DP[i] = result
    return DP[n]
print(countWaysToClimb([2,3], 7))