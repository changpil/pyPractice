
# Time o(nm) Space: O(nm)
import collections
def subString(s, sub):
    _dict = collections.defaultdict(list)
    for i in range(0, len(s)-len(sub)+1):
        candidates = s[i:i+len(sub)] # O(m)
        _dict[candidates].append(i)
    return _dict[sub][0] if _dict[sub] else -1

a ="abcdec"
b ="cd"
print(subString(a,b))
a ="abcdabzabcbcdbbcd"
b ="bcdb"
print(subString(a,b))

#######################          KMP substring O(n+m) O (n+m)    #######################

def buildPattern(p):
    trace = [0]*len(p)
    j = 0
    for i in range(1, len(p)):
        if p[i] == p[j]:
            j = j+1
            trace[i] = j
        else:
            lastIndex =  trace[j]
            while lastIndex > 0 and p[lastIndex] != p[i]:
                lastIndex = trace[lastIndex]
            trace[i] = lastIndex
            j = lastIndex

    return trace
# p = "abcdabc"
# print(buildPattern(p))
#
# p = "abcabczabdabc"
# print(buildPattern(p))
def substring(s, p):
    p = buildPattern(p)
    j = 0
    for i in range(len(s)-len(p) + 1):
        lastProcessed = i
        if s[i] == s[j]:
            j += 1
        else:
            j = p[j] + 1
        if j == len(p):
            break
    return lastProcessed

a ="abcdec"
b ="cd"
print(subString(a,b))

a ="ababcd"
b ="abcd"
print(substring(a,b))

a ="abcdabzabcbcdbbcd"
b ="bcdb"
print(subString(a,b))


