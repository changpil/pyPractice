"""
Given a list of strings return the substring representing the longest common prefix
"""

def longestCommonPrefix(strs):
    if strs == None or len(strs) < 1:
        return ""

    lcp = strs[0]
    for str_i in strs:
        prefix = ""
        for s in zip(lcp, str_i):
            if s[0] == s[1]:
                prefix += s[0]
            else:
                break
        if prefix == "":
            return ""
        else:
            lcp = prefix
    return lcp