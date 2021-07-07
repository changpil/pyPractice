"""
Longest Repeated Substring

Given a string inputStr of length n, find the longest repeated substring in it.
- Repeated substring is a substring that occurs more than once in the given string.
- If there are multiple such substrings of the same size, then return any one.
- If there are no repeated substrings, then return an empty string.

Example One
Input: “aaaa”

Output: “aaa”

aaa is the longest substring which is repeated in aaaa, starting at position 0 and starting at position 1.

Example Two
Input: “efabcdhefhabcdiefi”

Output: “abcd”

“abcd” repeats twice and “ef” repeats three times. Of those two repeated substrings, “abcd” is the longer one.

Example Three
Input: “abcdefghi”

Output: “”

There are no repeated substrings in “abcdefghi”.

Notes
Input Parameters: There is only one argument inputStr, denoting input string.

Output: Return a string lrs, denoting longest repeated substring.

Constraints:
2 <= n <= 2*10^5
inputStr may contain only lowercase characters a-z.

This is purely an exercise in building a Suffix Tree.
Suffix trees are difficult. You'd probably wonder if they really ask those in an interview.
They in fact are rarely asked, which is why we don't cover it in the class. But we've seen them at FB and Uber. In all occasions, it's been asked as a follow up question. Once you code up an N^2 algorithm for the problem on hand, there are a few minutes left, in which time, the interviewer would wonder if you know of Suffix trees. It is NEVER asked to implement one in an interview. That's stupid. If at that time, you do know of suffix trees, then you have a chance to convert that interviewer from a 3 (good) to a 4 (advocate). It suggests you have taken a keen interest in your prep work and by extension, in general CS.
Another reason we include it in the course: it is possibly one of the hardest data structures. Once you have a handle on it, a lot of other things will look easy ;-)
Doing difficult problems like these also has a strong ancillary benefit: it helps you indirectly interview your interviewer/company. You want to work for a team that challenges you; not the team that gives you a free pass.
Don't skimp on it. Take it head on, there are clear benefits.

Custom Input
Input Format: There should be only one line, containing inputStr, denoting input string.
If inputStr = “efabcdhefhabcdiefi”, then input should be:
efabcdhefhabcdiefi

Output Format: There will be only one line, containing a string lrs, denoting longest repeated substring.
For input inputStr = “efabcdhefhabcdiefi”, output will be:
abcd
"""


import collections
def getLongestRepeatedSubstring(inputStr):
    s = set()
    maxsub = (0, "")
    for i in range(len(inputStr) ):
        for j in range(i + 1, len(inputStr) + 1):
            tmp = inputStr[i:j]
            if  tmp in s:
                maxsub = (len(tmp) , tmp) if maxsub[0] < len(tmp) else maxsub
            else:
                s.add(tmp)
    return maxsub[1]
s = "aa"
print(getLongestRepeatedSubstring(s))

# s = "abcdefghi"
# print(getLongestRepeatedSubstring(s))
# s = "aaaa"
# print(getLongestRepeatedSubstring(s))
# inputStr = "efabcdhefhabcdiefi"
# print(getLongestRepeatedSubstring(inputStr))