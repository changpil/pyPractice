"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
"""

from collections import deque
def addStrings(num1, num2):
    h = {}
    for digit, ch in enumerate("0123456789"):
        h[ch] = digit

    n1 = 0

    for ch in num1:
        n1 = n1 * 10 + h[ch]

    n2 = 0
    for ch in num2:
        n2 = n2 * 10 + h[ch]

    s = n1 + n2
    # Miss s == 0.
    if s == 0:
        return "0"

    d = deque()
    r = {i: ch for ch, i in h.items()}

    while s:
        s, div = divmod(s, 10)
        d.appendleft(r[div])
    return "".join(d)

print(addStrings("0", "0"))