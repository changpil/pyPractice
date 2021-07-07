"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
"""
import time
# Time Exceeded
def divide(dividend, divisor ):
    sign = 1
    if dividend * divisor < 0:
        sign = -1
    if dividend == 0:
        return 0
    total, i = 0, 0
    while total <= abs(dividend):
        total += abs(divisor)
        i += 1
    return sign * (i - 1)

# print(divide(1234, -5))
#
# print(divide(-13, -2))
print(divide(7, -3))

def divide(dividend, divisor ):
    sign = 1
    if dividend * divisor < 0:
        sign = -1
    if dividend == 0:
        return 0
    base, mul, i = 0, abs(divisor), 1
    while mul  <= abs(dividend):
        base = 0 if mul == abs(divisor) else mul
        saved_mul = mul
        saved_i = i
        mul, i = abs(divisor), 1
        while base + mul + mul < abs(dividend):
            mul += mul
            i += i
        mul = saved_mul + mul
        i = saved_i + i
    MAX_INT = 2147483647  # 2**31 - 1
    MIN_INT = -2147483648  # -2**31
    quotient = sign * (i - 1)
    if quotient < MIN_INT:
        return MIN_INT
    if quotient > MAX_INT:
        return MAX_INT
    return quotient
# print(divide(1234, -5))# -246
# print(divide(-10, -3)) # 3
print(divide(-2147483648, 1)) # Expected (2147483647)
# print(divide(2147483647, 1)) # Expected (2147483647)
# print(divide(7, -3))