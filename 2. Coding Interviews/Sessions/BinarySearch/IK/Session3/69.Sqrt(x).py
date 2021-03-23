"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""


def mySqrt(x):
    start, end = 1, x//2 + 1
    while start <= end:
        mid = (start + end)//2
        if mid**2 <= x:
            start = mid + 1
        else:
            end = mid -1
    return end

print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(3))
print(mySqrt(4))
print(mySqrt(5))
print(mySqrt(6))
print(mySqrt(7))
print(mySqrt(8))
print(mySqrt(9))
print(mySqrt(10))
print(mySqrt(11))
print(mySqrt(12))
print(mySqrt(13))
print(mySqrt(14))
print(mySqrt(15))
print(mySqrt(16))