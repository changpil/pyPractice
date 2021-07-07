"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

"""


def partitionLabels(s):
    i = 0
    j = 0
    result = []
    while j < len(s):
        j = getIndex(s, s[j])
        for k in range(i, j+1):
            j = max(j, getIndex(s, s[k]))
        result.append(j + 1 - i)
        i = j + 1
        j = j + 1
    return result

def getIndex(s, c):
    for i in range(len(s) -1, -1, -1):
        if s[i] == c:
            return i
    return -1


s = "ababcbacadefegdehijhklij"
print(partitionLabels(s))