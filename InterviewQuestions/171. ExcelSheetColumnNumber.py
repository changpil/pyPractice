# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701


def titleToNumber(s: str) -> int:
    digits = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = len(s) -1
    result = 0
    for ch in s:
        n = digits.index(ch)

        result += n*26**index
        index -= 1
    return result

## 28
print(titleToNumber("AB"))
#701
print(titleToNumber("ZY"))