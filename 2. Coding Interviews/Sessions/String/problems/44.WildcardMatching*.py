"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false

"""
def isMatch(s, p):
    if s == p:
        return True
    # remove duplicated * like **, ***

    return _ismatch(s, 0, p, 0)

def _ismatch(s, i, p, j):
    if i == len(s) and j == len(p):
        return True
    if i == len(s) or j == len(p):
        if i == len(s) and j == len(p) -1 and p[j] == "*":
            return True
        else:
            return False
    if p[j] == "*":
        return _ismatch(s, i + 1, p, j) or _ismatch(s, i, p, j+1)
    elif p[j] == "?":
        return _ismatch(s, i+1, p, j+1)
    else:
        if s[i] != p[j]:
            return False
        else:
            return _ismatch(s, i+1, p, j+1)
# s = "aa"
# p = "a"
# print(isMatch(s,p))
#
# s = "aa"
# p = "*"
# print(isMatch(s,p))
#
# s = "cb"
# p = "?a"
# print(isMatch(s,p))
#
# s = "adceb"
# p = "*a*b"
# print(isMatch(s,p))
#
# s = "acdcb"
# p = "a*c?b"
# print(isMatch(s,p))
#
#
# s = "acdcb"
# p = "*?*"
# print(isMatch(s,p))

