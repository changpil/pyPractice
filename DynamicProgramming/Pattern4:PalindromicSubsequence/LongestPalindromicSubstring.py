# Problem Statement #
# Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.
#
# Example 1:
#
# Input: "abdbca"
# Output: 3
# Explanation: LPS is "bdb".
# Example 2:
#
# Input: = "cddpd"
# Output: 3
# Explanation: LPS is "dpd".
# Example 3:
#
# Input: = "pqr"
# Output: 1
# Explanation: LPS could be "p", "q" or "r".
def isPalindromic(st):
    i, j = 0, len(st)-1
    while i < j:
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    return True

# O(N)
def longestSubstring(st):
    start, end= -1,-1
    for i in range(len(st)):
        j = len(st) -1
        while i < j:
            if isPalindromic(st[i:j+1]):
                if end - start < j -i :
                    start, end  = i, j
            j -= 1

    return st[start:end+1]


print(longestSubstring("abdbca"))
print(longestSubstring("cddpd"))
print(longestSubstring("pqr"))

def pal_substring(st):
    return _pal_substring(st, 0, len(st)-1)

def _pal_substring(st, start, end):
    if isPalindromic(st[start:end+1]):
        return end - start + 1
    if start > end:
        return 0

    r1 = _pal_substring(st,start +1, end)
    r2 = _pal_substring(st, start, end -1)
    return max(r1, r2)

print(pal_substring("abdbca"))
print(pal_substring("cddpd"))
print(pal_substring("pqr"))


# Educative
def pal_substring(st):
    return _pal_substring(st, 0, len(st)-1)

def _pal_substring(st, start, end):
    if start > end :
        return

    if start == end:
        return 1

    if st[start] == st[end]:
        remainingLength = end - start -1
        if remainingLength == _pal_substring(st, start +1, end -1):
            return remainingLength + 2
    r1 = _pal_substring(st,start +1, end)
    r2 = _pal_substring(st, start, end -1)
    return max(r1, r2)

print(pal_substring("abdbca"))
print(pal_substring("cddpd"))
print(pal_substring("pqr"))