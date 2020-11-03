"""
"123" --> 123


case for "-123"
"""

def conversion(_str):
    negative = 1
    if _str[0] =="-":
        negative = -1
        _str = _str[1:]
    result = 0
    for digit in _str:
        if not digit.isdigit():
            raise ValueError
        result *= 10
        result += ord(digit) - ord('0')
    return result* negative

print(conversion("-0"))