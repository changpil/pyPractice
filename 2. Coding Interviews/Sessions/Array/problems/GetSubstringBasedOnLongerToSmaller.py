

def getSubstrings(s):
    gap = len(s)
    result = []
    while gap > 0 :
        i, j = 0, gap
        while j < len(s):
            result.append(s[i:j])
            j += 1
            i += 1
        gap -= 1
    return result

s = "hello world"
print(getSubstrings(s))