"""
Given a string S, return the number of substrings of length K with no repeated characters.



Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation:
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation:
Notice K can be larger than the length of S. In this case is not possible to find any substring.
"""

import collections
def numKLenSubstrNoRepeats(S, K):
    duplicatedChar = collections.defaultdict(lambda : 0)
    nOfNonRepeatedCharString = 0
    for i in range(min(K, len(S))):
        duplicatedChar[S[i]] += 1

    if len(duplicatedChar) == K:
        nOfNonRepeatedCharString += 1
    for i in range(K, len(S)):
        duplicatedChar[S[i]] += 1
        if duplicatedChar[S[i-K]] == 1:
            duplicatedChar.pop(S[i-K])
        else:
            duplicatedChar[S[i - K]] -= 1
        if len(duplicatedChar) == K:
            nOfNonRepeatedCharString += 1

    return nOfNonRepeatedCharString


S = "havefunonleetcode"
# 6
print(numKLenSubstrNoRepeats(S, 5))

S= "home"
# 0
print(numKLenSubstrNoRepeats(S, 5))