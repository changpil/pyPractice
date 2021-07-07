"""
A perfect square is a number made by squaring a whole number.

Some examples include 1, 4, 9, or 16, and so on -- because they are the squared results of 1, 2, 3, 4, etc. For example:

SNIPPET
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
...
Given some positive integer n, write a method to return the fewest number of perfect square numbers which sum to n.

The follow examples should clarify further:

JAVASCRIPT
var n = 28
howManySquares(n);
// 4
// 16 + 4 + 4 + 4 = 28, so 4 numbers are required
// Not 25 + 1 + 1 + 1
On the other hand:

JAVASCRIPT
var n = 16
howManySquares(n);
// 1
// 16 itself is a perfect square
// so only 1 perfect square is required
Constraints
n <= 10000
n will always be non zero positive integer
Expected time complexity : O(n*sqrt(n))
Expected space complexity : O(n)
"""

# from math import sqrt, ceil
import math


def howManySquares(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    sub = math.floor(math.sqrt(n))
    minv = math.inf
    for i in range(1, sub + 1):
        minv = min(minv, howManySquares(n - i ** 2) + 1)
    return minv


import time

start = time.time()
for i in range(33, 34):
    print("$" * 10, i, "$" * 10)
    print(howManySquares(i))
end = time.time()
print(end - start)


# print(howManySquares(28))
# print(howManySquares(52))

def getPairs(n):
    for i in range(1, n // 2 + 1):
        yield i, n - i


def howManySquares(n):
    dp = [-1] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(2, n + 1):
        if math.ceil(math.sqrt(i))**2 == i:
            dp[i] = 1
        else:
            localmin = math.inf
            for a, b in getPairs(i):
                localmin = min(localmin, dp[a] + dp[b])
            dp[i] = localmin
    print(dp)
    return dp[-1]


start = time.time()
for i in range(33, 34):
    print("$" * 10, i, "$" * 10)
    print(howManySquares(i))
end = time.time()
print(end - start)
