# Problem Statement #
# Given a string, find the length of the longest substring, which has no repeating characters.
#
# Example Pattern1:knapsack:
#
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:
#
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:
#
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".


# Brute Force way o(n^2)
# The worst case orf Brute force "abcdefghi"

# Sliding window 0(n)

def longestUniqueSubstring(chars):
    noc, start = 0,0
    s = set()
    for end in range(len(chars)):
        while chars[end] in s:
            s.remove(chars[start])
            start += 1
        s.add(chars[end])
        noc = max(noc, end - start +1)
    return noc

print(longestUniqueSubstring("aabccbb"))
print(longestUniqueSubstring("abbbb"))
print(longestUniqueSubstring("abccde"))
print(longestUniqueSubstring("abcdef"))
print(longestUniqueSubstring("aaabbbbccc"))