"""
Operations: Replace, Insert, Delete

hourse - > ros
Edit distance: 3
hourse _> rorse
rorse -> rose
rose -> ros
"""

import math
def editDistance(str1, str2):
    return _editDistance(str1, 0, str2, 0)
def _editDistance(str1, i, str2, j):
    if i == len(str1) and j == len(str2):
        return 0
    # THIS IS WRONG LOGIC: If one str is ended, we need to insert or delete/
    # if i == len(str1) or j == len(str2):
    #     return math.inf
    if i == len(str1):
        return len(str2) - j
    if j == len(str2):
        return len(str1) - i

    if str1[i] == str2[j]:
        return _editDistance(str1, i+1, str2, j+1)
    else:
        _re = _editDistance(str1, i+1, str2, j+1)
        _in = _editDistance(str1, i, str2, j+1)
        _de = _editDistance(str1, i+1, str2, j)
    return min(_re, _in, _de) + 1

print(editDistance("horse", "ros"))
print(editDistance("sunday", "saturday"))

def editDistanceDP(str1, str2):
    dp =[ [0]*(len(str1) + 1) for _ in range(len(str2) + 1)]
    dp[0][0] = 0
    for i in range(1, len(dp)):
        dp[i ][0] = i
    for j in range(1, len(dp[0])):
        dp[0][ j ] = j

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str2[i-1] == str1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    # for row in dp:
    #     print(row)
    return dp[-1][-1]
print(editDistanceDP("horse", "ros"))
print(editDistanceDP("sunday", "saturday"))



