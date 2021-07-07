"""
Longest Substring With Exactly Two Distinct Characters
Given a string s of length n, find the length of the longest substring ss, that contains exactly two distinct characters.
There will be t test cases.

Example One
Input:
2
eceba
abcdef

Output:
3
2

In the first case, 'ece' is the largest substring with exactly 2 distinct characters.
In the second case, 'ab' is the largest substring with exactly 2 distinct characters. Also, 'bc', 'cd', 'de', 'ef' can be considered as substring with exactly 2 distinct characters.

Example Two
Input:
3
ababababa
e
baabcbab

Output:
9
0
4

In the first case, the whole string 'ababababa' is the largest substring with exactly 2 distinct characters.
In the second case, there is no substring with exactly 2 distinct characters.
In the third case, 'baab' is the largest substring with exactly 2 distinct characters.

Notes
Input Parameters: There is only one argument s, denoting the input string.

Output: Return an integer len, denoting length of ss.
(If there are no such substrings, then return 0)

Constraints:
1 <= t <= 80
1 <= n <= 10^5
s may contain upper case alphabets, lower case alphabets and numerical values.

Custom Input
Input Format: The first line of the input should contain an integer t, denoting no. of test cases.
In the next t lines, ith line should contain a string si, denoting an input string s for ith test case.
If t = 3, s for 1st test case = “ababababa”, s for 2nd test case = “e” and s for 3rd test case = “baabcbab”, then input should be:
3
ababababa
e
baabcbab

Output Format: There will be t lines for output, where ith line contains an integer leni, denoting resultant value len for ith test case. For input t = 3, s for 1st test case = “ababababa”, s for 2nd test case = “e” and s for 3rd test case = “baabcbab”, output will be:
9
0
"""


# Complete the getLongestSubstringLengthExactly2DistinctChars function below.
import collections
def getLongestSubstringLengthExactly2DistinctChars(s):
    dc = collections.defaultdict(lambda: 0)
    maxwindow = 0
    start = 0
    for i in range(len(s)):
        dc[s[i]] += 1
        while start <= i and len(dc) > 2:
            dc[s[start]] -= 1
            if dc[s[start]] == 0:
                dc.pop(s[start])
            start += 1
        if len(dc) == 2:
            maxwindow = max(maxwindow, i- start + 1)
    return maxwindow
s = "ababababa"
print(getLongestSubstringLengthExactly2DistinctChars(s))
s = "e"
print(getLongestSubstringLengthExactly2DistinctChars(s))
s = "baabcbab"
print(getLongestSubstringLengthExactly2DistinctChars(s))


