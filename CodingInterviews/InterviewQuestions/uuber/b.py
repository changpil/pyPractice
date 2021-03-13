def binaryPatternMatching(pattern, s):
    vowels = {'a', 'e', 'i','o','u'}
    if len(pattern) > len(s):
        return 0
    matched = 0
    for i in range(0,len(s) - len(pattern) + 1):
        s_start = i
        p_start = 0
        re = True
        while p_start < len(pattern):
            if pattern[p_start] == 0 and s[s_start] not in vowels:
                re = False
                break
            elif pattern[p_start] == 1 and s[s_start] in vowels :
                re = False
                break
            p_start += 1
            s_start += 1
        if re:
            matched += 1
    return matched

binaryPatternMatching("010", "amazing")