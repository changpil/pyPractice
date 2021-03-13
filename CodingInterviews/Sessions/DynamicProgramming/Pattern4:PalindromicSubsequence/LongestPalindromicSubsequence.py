# Problem Statement #
# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.
#
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
#
# Example 1:
#
# Input: "abdbca"
# Output: 5
# Explanation: LPS is "abdba".
# Example 2:
#
# Input: = "cddpd"
# Output: 3
# Explanation: LPS is "ddd".
# Example 3:
#
# Input: = "pqr"
# Output: 1
# Explanation: LPS could be "p", "q" or "r".

# O(n^n)
def longestSubsequence(string):
    if isPalindromic(string):
        return string

    longest = ""
    for i in range(len(string)):
        p =  longestSubsequence(string[:i] + string[i+1:])
        longest = p if len(p) > len(longest) else longest
    return longest

def isPalindromic(string):
    i, j = 0, len(string)-1
    while i  < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

print(longestSubsequence("abdbca"))
print(longestSubsequence("cddpd"))
print(longestSubsequence("pqr"))

# Educative

# O(2^N)
def find_LPS(st):
  return _LPS(st, 0, len(st) - 1)

def _LPS(st, start, end):
  if start > end:
    return ""

  if start == end:
    return st[start]

  if st[start] == st[end]:
    return  st[start] + _LPS(st, start + 1, end - 1) + st[start]

  c1 = _LPS(st, start + 1, end)
  c2 = _LPS(st, start, end - 1)
  return c1 if len(c1) > len(c2) else c2

print(longestSubsequence("abdbca"))
print(longestSubsequence("cddpd"))
print(longestSubsequence("pqr"))