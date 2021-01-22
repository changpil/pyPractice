"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -Pattern1:knapsack.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

## This should be taken as a cautious aproach




#Does this have lowercase and uppercase

#case1 : s
#case2 : ss
#case  : abc
#case  : abcdabc
#case  : abccba

#Pattern1:knapsack     Solution of O(n)
def firstUniqueChar(s):
    data = dict()
    for i, c in enumerate(s):
        indexies = data.get(c, [])
        indexies.append(i)
        data[c] = indexies

    unique_indexes=[]
    for v in data.values():
        if len(v) == 1:
            unique_indexes.extend(v)

    if len(unique_indexes) == 0:
        return -1
    else:
        return min(unique_indexes)


#print(firstUniqueChar("aas"))

#2     Solution of O(n^2)

def firstUniqueChar2(s):

    for i in range(len(s)):
        no_dup = True
        for j in range(len(s)):
            if i == j:
                continue
            if s[i] == s[j]:
                no_dup = False
                break;
        if no_dup:
            return i

    return -1


print(firstUniqueChar2("cc"))