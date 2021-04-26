
def subset(l):
    subsets = set()
    word = "".join(l)
    _subset(word, subsets, len(word) )
    return subsets

def _subset(word, subsets, level):
    if level == 0:
        return subsets.add("")
    subsets.add(word)
    for i in range(0, len(word)):
        disect_w = word[:i] + word[i+1:]
        _subset(disect_w, subsets, level -1)

def getallSubstrings(s):
    allsubs = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            allsubs.append(s[i:j])
    return allsubs

def getSubs(s):
    allsubs = []

    for i in range(1, len(s)):
        end = len(s) - i
        for start in range(end + 1):
            allsubs.append(s[start:start + i])
    return allsubs

s=["a", "b", "c"]
print(subset(s))

s = "abc"
print(getallSubstrings(s))

s = "abc"
print(getSubs(s))

#
# s=["c", "b", "a"]
# print(subset(s))
#
# s = "cba"
# print(getallSubstrings(s))


s=["a", "b", "c", "d"]
print(subset(s))

s = "abba"
print(getallSubstrings(s))

s = "abba"
print(getSubs(s))