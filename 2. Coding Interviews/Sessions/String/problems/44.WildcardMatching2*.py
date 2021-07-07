"""
Regex Matcher
Given a text string containing characters only from lowercase alphabetic characters and a pattern string containing characters only from lowercase alphabetic characters and two other special characters '.' and '*'.
Your task is to implement a pattern matching algorithm that returns true if pattern is matched with text otherwise returns false. The matching must be exact, not partial.
Explanation of the special characters:
1) '.' - Matches a single character from lowercase alphabetic characters.
2) '*' - Matches zero or more preceding character. It is guaranteed that '*' will have one preceding character which can be any lowercase alphabetic character or special character '.'. But '*' will never be the preceding character of '*'. (That means "**" will never occur in the pattern string.)
'.' = "a", "b", "c", ... , "z".
a* = "a","aa","aaa","aaaa",... or empty string("").
ab* = "a", "ab", "abb", "abbb", "abbbb",...
Example One
Input: text = "abbbc" and pattern = "ab*c"
Output: true
Given pattern string can match:
"ac", "abc", "abbc", "abbbc", "abbbbc", ...
Example Two
Input: text = "abcdefg" and pattern = "a.c.*.*gg*"
Output: true
".*" in pattern can match  "", ".", "..", "...", "....", ...
"g*" in pattern can match "", "g", "gg", "ggg", "gggg", ...
Now, consider:
    '.' at position 2 as 'b',
    '.*'  at position {4,5} as "...",
    '.*' at position {6,7} as "" and
    [g*] at position {8,9} as "".
So, "a.c.*gg*" = "abc...g" where we can write "..." as "def". Hence, both matches.
Example Three
Input:
text = "abc" and pattern = ".ab*.."
Output: false
If we take 'b*' as "" then also, length of the pattern will be 4 (".a.."). But, given text's length is only 3. Hence, they can not match.
"""

# OUT OF TIME
def pattern_matcher(text, pattern):
	# Normalize **,*** in pattern
	return foo(text, 0, pattern, 0)
	
def foo(text, i, pattern, j):
    if i == len(text) and j == len(pattern):
        return True
        
    if i == len(text) and j != len(pattern):
        if j < len(pattern) - 1 and pattern[j+1] == "*":
            return foo(text, i, pattern, j + 2)
        else:
            return False

    if i != len(text) and j == len(pattern):
        return False

    if  pattern[j] != ".":
        if j < len(pattern) - 1 and pattern[j + 1] == "*":
                return foo(text, i + 1, pattern, j) or foo(text, i, pattern, j + 2)
        else:
            if text[i] != pattern[j]:
                return False
            else:
                return foo(text, i + 1, pattern, j + 1)

    else:
        if j < len(pattern) - 1 and pattern[j + 1] == "*":
            return foo(text, i + 1, pattern, j) or foo(text, i, pattern, j + 2)
        else:
            return foo(text, i + 1, pattern, j + 1)

# s = "abbbc"
# p = "ab*c"
# print(pattern_matcher(s, p))
#
# s = "abcdefg"
# p = "a.c.*.*gg*"
# print(pattern_matcher(s, p))

# s = ""
# p = "a*b*c*.*g*"
# print(pattern_matcher(s, p))
"""
BUG Fixed
    if i == len(text) and j != len(pattern):
        if j == len(pattern) - 2 and pattern[j+1] == "*":
            return True
        else:
            return False
"""


def pattern_matcher(text, pattern):
    dp = [[False]*(len(pattern) + 1) for _ in range(len(text) + 1)]
    dp[0][0] = True
    for j in range(1, len(dp[0])):
        if j < len(pattern) and pattern[j] == "*":
            dp[0][j] = dp[0][j -1]
        elif pattern[j-1] == "*":
            dp[0][j] = dp[0][j - 1]
        else:
            dp[0][j] = False

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if pattern[j-1] == "*":
                    dp[i][j] = dp[i][j-1]
            elif "a" <= pattern[j-1] <= "z":
                if j < len(pattern) and pattern[j] != "*":
                    dp[i][j] = dp[i -1][j-1] and text[i-1] == pattern[j-1]
                elif j < len(pattern) and pattern[j] == "*":
                    dp[i][j] = (dp[i - 1][j] and text[i - 1] == pattern[j - 1]) or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i-1][j-1] and text[i-1] == pattern[j-1]
            elif pattern[j-1] == ".":
                if j < len(pattern) and pattern[j] != "*":
                    dp[i][j] = dp[i - 1][j-1]
                elif j < len(pattern) and pattern[j] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1]
    for l in dp:
        print(l)
    return dp[-1][-1]

s = "abbbc"
p = "ab*c"
print(pattern_matcher(s, p))
#
s = "abcdefg"
p = "a.c.*.*gg*"
print(pattern_matcher(s, p))

s = ""
p = "a*b*c*.*g*"
print(pattern_matcher(s, p))
