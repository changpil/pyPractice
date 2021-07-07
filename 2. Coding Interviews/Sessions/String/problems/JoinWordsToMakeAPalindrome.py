"""
Join Words To Make A Palindrome

Given a list of strings words, of size n, check if there is any pair of words that can be joined (in any order) to form a palindrome then return the pair of words forming palindrome.

Example One
Input: words = [ “bat”, “tab”, “zebra” ]

Output: result = [ “bat”, “tab” ]

As “bat” + “tab” = “battab”, which is a palindrome.

Example Two
Input: words = [ “ant”, “dog”, “monkey” ]

Output: result = [ “NOTFOUND”, “DNUOFTON” ]

As for each 6 combinations of string of words, there is no single generated word which is a palindrome hence result list will be [ “NOTFOUND”, “DNUOFTON” ].

Notes
Input Format: Only argument for function, list of strings words.

Output:
Return a pair of words (i.e. list of string result of size 2 such that result[0] + result[1] is a palindrome).
In case of multiple answers return any one of them.
In case of no answer return list [“NOTFOUND”, “DNUOFTON”].

Constraints:
Length l for each word of words list, 1<= l <= 30.
Size of list words n, 2 <= n <= 20000.
Characters for each word can be from [a-z], [A-Z], [0-9].
"""
import collections
#time limit exceeded
def join_words_to_make_a_palindrome(words):
    com = collections.defaultdict(lambda: [])

    for i in range(len(words)):
        for j in range(i + 1,len(words)):
            word = words[i] + words[j]
            rword = words[j] + words[i]
            com[word].append([words[i], words[j]])
            com[rword].append([words[j], words[i]])
    for key in com:
        if isPalindrome(key):
            return com[key][0]
    return [ "NOTFOUND", "DNUOFTON" ]

def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
def join_words_to_make_a_palindrome(words):
    com = collections.defaultdict(lambda: [])

    for i in range(len(words)):
        for j in range(i + 1,len(words)):
            if words[i][0] == words[j][-1]:
                word = words[i] + words[j]
                com[word].append([words[i], words[j]])
            if words[j][0] == words[i][-1]:
                rword = words[j] + words[i]
                com[rword].append([words[j], words[i]])

    for key in com:
        if isPalindrome(key):
            return com[key][0]
    return [ "NOTFOUND", "DNUOFTON" ]


words = [ "bat", "tab", "zebra" ]
print(join_words_to_make_a_palindrome(words))