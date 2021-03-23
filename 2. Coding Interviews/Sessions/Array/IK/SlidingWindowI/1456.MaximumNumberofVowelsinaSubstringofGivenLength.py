"""
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).
"""
def maxVowels(s, k):
    numVowels = 0
    vowels = {'a', 'e','i','o','u'}
    for i in range(min(k, len(s))):
        if s[i] in vowels:
            numVowels += 1
    maxVowel = numVowels
    for i in range(k, len(s)):
        if s[i] in vowels:
            numVowels += 1
        if s[i-k] in vowels:
            numVowels -= 1
        maxVowel = max(maxVowel, numVowels)

    return maxVowel

s = "abciiidef"
print(maxVowels(s, 3))