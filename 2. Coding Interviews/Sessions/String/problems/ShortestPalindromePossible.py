"""
We have a string str like the following:

JAVASCRIPT
const str = "bubble";
Find a way to convert it to a palindrome by inserting characters in front of it. Recall that a palindrome is defined as "a word, phrase, or sequence that reads the same backward as forward".


What's the shortest palindrome that can be returned? For example, the following above string should return:

JAVASCRIPT
shortestPalindrome("bubble")
// "elbbubble"
"""

def shortestPalindrome(s):
    i, j  = 0, len(s) - 1
    lastIndex = 0
    while i < j:
        ii, jj = i, j
        while ii < jj and s[ii] == s[jj]:
            ii += 1
            jj -= 1
        if ii >= jj:
            lastIndex = j
            break
        j -= 1
    return "".join(list(s[lastIndex+1:])[::-1]) + s

s = "bubble"
print(shortestPalindrome(s))
