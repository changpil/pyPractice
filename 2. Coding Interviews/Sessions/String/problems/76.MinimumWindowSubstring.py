"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
import math
import collections
def minWindow(str, pat):
    d = collections.defaultdict(lambda: 0)
    i, j = 0, 0
    lettermap = collections.defaultdict(lambda: 0)
    for c in pat:
        lettermap[c] += 1

    # while j <len(str) and not isfilled(d, lettermap):
    #     if str[j] in lettermap.keys():
    #         d[str[j]] += 1
    #     j += 1
    # if isfilled(d, lettermap):
    #     minIndex = (j, (0, j))
    # else:
    #     return ""
    minIndex = (math.inf, (0,0))
    while j < len(str):
        print(d)
        if str[j] in lettermap.keys():
            d[str[j]] += 1
        while i <= j and isfilled(d, lettermap):
            if minIndex[0] > j-i +1:
                minIndex = (j -i + 1, (i, j+1))
            d[str[i]] -= 1
            i += 1
        j += 1
    # Check for no matching
    return str[minIndex[1][0]: minIndex[1][1]]

def isfilled(c, d):
    for l in d:
        if d[l] > c[l]:
            return False
    return True

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))