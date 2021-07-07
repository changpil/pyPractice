"""
str1 = "hello my name is chang"
str2 = "what is your name"
output:" name"
"""
# 2^N
def allSubset(str):
    store = []
    _allSubset(str, 0, "", store)
    return store

def _allSubset(str, i, tmp, store):
    if i >= len(str):
        store.append(tmp)
        return
    _allSubset(str, i + 1, tmp, store)
    tmp += str[i]
    _allSubset(str, i + 1, tmp, store)

s = "abcd"
print(allSubset(s))

#O(N^3)
def allSubstring(str):
    store = []
    for i in range(len(str)):
        for j in range(i+1, len(str) + 1):
            store.append(str[i:j])
    return store

s = "abcd"
print(allSubstring(s))
# O(n^3 )
import math
def substringMatch(s1, s2):
    s1 = set(allSubstring(s1))
    s2 = set(allSubstring(s2))

    longest = (-math.inf, None)
    for w1 in s1:
        if w1 in s2 and len(w1) > longest[0]:
            longest = (len(w1), w1)
    return longest[1]

s1 = "abcd"
s2 = "bc"
print(substringMatch(s1, s2))


# If you build suffix Trie, it can be O(N + M)
