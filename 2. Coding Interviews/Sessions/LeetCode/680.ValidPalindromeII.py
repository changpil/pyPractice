# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Time Limit Exceeded
# def isPal(s):
#     i, j = 0, len(s) - 1
#     while i < j:
#         if s[i] != s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
#
# def validPalindrome(s):
#     if isPal(s):
#         return True
#
#     for i in range(len(s)):
#         onelesss = s[:i] + s[i + 1:]
#         if isPal(onelesss):
#             return True
#     return False

def validPalindrome(s):
    return helper(s, 0, len(s) -1, 1)

def helper(s, i, j, allowance):
    if allowance < 0:
        return False

    if i >= j:
        return True

    if s[i] == s[j]:
        return helper(s, i+1, j -1, allowance)
    else:
        left = helper(s, i+1, j, allowance -1)
        right = helper(s, i, j-1, allowance -1)

        if right or left:
            return True

print(validPalindrome("abaa"))

