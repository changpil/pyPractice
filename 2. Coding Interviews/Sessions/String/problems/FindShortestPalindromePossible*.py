"""
We have a string str like the following:

JAVASCRIPT
const str = "bubble";
Find a way to convert it to a palindrome by inserting characters in front of it. Recall that a palindrome is defined as "a word, phrase, or sequence that reads the same backward as forward".


What's the shortest palindrome that can be returned? For example, the following above string should return:

JAVASCRIPT
shortestPalindrome("bubble")
// "elbbubble"
Constraints
Length of the given string <= 1000
The string can contain any ASCII letters
Expected time complexity : O(n)
Expected space complexity : O(1)
"""
# Time Limit Exceeded
# def shortestPalindrome(s):
#     leastIndex = len(s) - 1
#     for i in range(len(s)-1, -1, -1):
#         f = 0
#         leastIndex = i
#
#         while f <= i and s[f] == s[i]:
#             f += 1
#             i -= 1
#         if f > i:
#             break
#     return "".join(list(s[leastIndex + 1:])[::-1]) + s


# print(shortestPalindrome("bubble"))
# s = "aacecaaa"


def shortestPalindrome(s):
    j = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            j += 1
    if j == len(s):
        return s
    palindromeEnd = s[j:]
    print(palindromeEnd)
    return "".join(list(palindromeEnd)[::-1]) + shortestPalindrome(s[0:j]) + palindromeEnd



# print(shortestPalindrome("abcd"))
# print(shortestPalindrome("aabc"))
# print(shortestPalindrome("aaaa"))
# print(shortestPalindrome("aabac"))

print(shortestPalindrome("butbbb"))