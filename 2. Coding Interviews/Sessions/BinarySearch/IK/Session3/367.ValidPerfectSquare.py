"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false

"""


def isPerfectSquare(num):
    start, end = 1, num//2 + 1
    while start <= end:
        mid = (start + end)//2
        if mid **2 == num:
            return True
        elif mid **2 > num:
            end = mid -1
        else:
            start = mid + 1
            
    return False

print(isPerfectSquare(1))
print(isPerfectSquare(2))
print(isPerfectSquare(3))
print(isPerfectSquare(4))
print(isPerfectSquare(5))
print(isPerfectSquare(6))
print(isPerfectSquare(7))
print(isPerfectSquare(8))
print(isPerfectSquare(9))
print(isPerfectSquare(10))
print(isPerfectSquare(11))
print(isPerfectSquare(12))
print(isPerfectSquare(13))
print(isPerfectSquare(14))
print(isPerfectSquare(15))
print(isPerfectSquare(16))
