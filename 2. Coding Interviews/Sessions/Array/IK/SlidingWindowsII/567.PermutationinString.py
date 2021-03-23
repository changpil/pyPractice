"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""
import collections

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    map = collections.defaultdict(lambda: 0)
    map2 = collections.defaultdict(lambda: 0)
    for c in s1:
        map[c] += 1
    k = len(s1)
    for i in range(k):
        map2[s2[i]] += 1

    if map == map2:
        return True

    for i in range(k, len(s2)):
        map2[s2[i]] += 1
        map2[s2[i-k]] -= 1
        if map2[s2[i-k]] == 0:
            map2.pop(s2[i-k])
        if map == map2:
            return True
    return False

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))

s1= "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))