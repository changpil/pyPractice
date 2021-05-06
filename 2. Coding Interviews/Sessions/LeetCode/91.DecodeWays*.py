"""

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
Example 4:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
"""
mapper = {f"{i}":chr(ord("A") + i - 1)  for i in range(1, 27)}

# def numDecodings(s):
#     store = [0]
#     memo = {}
#     help(s, 0, store)
#     if len(store) == 0:
#         return 0
#     return store[0]
#
# def help(s,index, store):
#     if index == len(s):
#         store[0] += 1
#         return
#     if index > len(s):
#         return
#     if s[index] in mapper:
#         help(s, index +1, store)
#
#     if index + 2 <= len(s) and s[index:index+2] in mapper:
#         help(s, index + 2, store)

# I DID NOT NOTICE THIS SI A DP PROBLEM UNTIL I SEE THE SOLUTION AND TIMEOUT FROM RECURSION
def numDecodings(s):
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    # Ways to decode a string of size 1 is 1. Unless the string is '0'.
    # '0' doesn't have a single digit decode.
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, len(dp)):

        # Check if successful single digit decode is possible.
        if s[i - 1] in mapper:
            dp[i] += dp[i - 1]

        # Check if successful two digit decode is possible.
        if i-2 >= 0 and s[i - 2: i] in mapper:
            dp[i] += dp[i - 2]

    return dp[-1]



# s = "12"
# print(numDecodings(s))
#
s = "22"
print(numDecodings(s))

s= "016"
print(numDecodings(s))

s= "111111111111111111111111111111111111111"
print(numDecodings(s))

## Time Limit Exceeded
# s= "111111111111111111111111111111111111111111111"
# print(numDecodings(s))