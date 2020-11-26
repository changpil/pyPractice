# Problem Statement #
# Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.
#
# Example 1:
#
# Input: "abdbca"
# Output: 3
# Explanation: Palindrome pieces are "a", "bdb", "c", "a".
# Example 2:
#
# Input: = "cddpd"
# Output: 2
# Explanation: Palindrome pieces are "c", "d", "dpd".
# Example 3:
#
# Input: = "pqr"
# Output: 2
# Explanation: Palindrome pieces are "p", "q", "r".
# Example 4:
#
# Input: = "pp"
# Output: 0
# Explanation: We do not need to cut, as "pp" is a palindrome.


def minimum_palindromic_partition(st):
    return _minimum_palindromic_partition(st, 0, len(st)-1)

def _minimum_palindromic_partition(st, start, end):
    if start >= end:
        return 0

    m1, m2 ,m3 = len(st)-1, len(st) -1, len(st) -1

    if st[start] == st[end]:
        m1 = _minimum_palindromic_partition(st, start +1, end -1)
        if m1 != 0:
            m1 += 2
    m2 = _minimum_palindromic_partition(st, start +1, end)
    m3 = _minimum_palindromic_partition(st, start, end -1)
    m2 += 1
    m3 += 1
    return min(m1, m2, m3)

print(minimum_palindromic_partition("abdbca"))
print(minimum_palindromic_partition("cddpd"))
print(minimum_palindromic_partition("pqr"))
print(minimum_palindromic_partition("pp"))