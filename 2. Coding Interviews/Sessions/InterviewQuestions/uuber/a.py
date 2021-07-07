def boundedRatio(a, l, r):
    re = []
    for i in range(len(a)):
        if a[i]%(i+1) != 0:
            re.append(False)
        elif l <= a[i]//(i+1) <= r:
            re.append(True)
        else:
            re.append(False)
    return re

def binaryPatternMatching(pattern, s):
    vowels = {'a', 'e', 'i','o','u', 'y'}
    if len(pattern) > len(s):
        return 0
    matched = 0
    for i in range(0,len(s) - len(pattern) + 1):
        s_start = i
        p_start = 0
        re = True
        while p_start < len(pattern):
            if pattern[p_start] == "0" and s[s_start] not in vowels:
                re = False
                break
            elif pattern[p_start] == "1" and s[s_start] in vowels :
                re = False
                break
            p_start += 1
            s_start += 1
        if re:
            matched += 1
    return matched

def segmentsWithSum(a, m, k):
    matched = 0
    for i in range(len(a) -m +1):
        if check( a[i: i+ m], k):
           matched += 1
    return matched
def check(a, k):
    for i in range(len(a)):
        for j in range(i +1, len(a)):
            if a[i] + a[j] >= k:
                return True
    return False
