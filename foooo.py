import collections
def getSubs(s):
    ss = collections.defaultdict(lambda: set())
    for i in range(len(s)):
        for l in range(1, len(s)):
            for start in range(i, len(s)-l+1):
                sub = "".join(sorted(s[start: start + l]))
                ss[sub].add((start, start+l))
    #print(ss)
    counter = 0
    for key in ss:
        if len(ss[key]) > 1:
            for n  in range(1, len(ss[key])):
                counter += n
    return counter

s = "abba"
print(getSubs(s))

s = "kkkk"
print(getSubs(s))