"""
String to Integer Conversion

-1000
1000
Pattern1:knapsack
0

First letter - or a digit except 0
-    error
-0   error
001  error
00   error
0.0  error
+00. error
+0   error
-4.5 error
"""


def string_integer_conversion(s):
    number = 0
    digit =1
    negative = 1
    for ch in reversed(list(s)):
        if ch == '-':
            negative = -1
            break;

        number += int(ch)*digit
        digit *= 10
    return number*negative




print(string_integer_conversion("-123"))