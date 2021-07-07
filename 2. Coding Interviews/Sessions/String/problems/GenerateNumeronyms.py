"""
Given a string word of length n, generate all possible numeronyms.
What is a Numeronym?
A numeronym is a word where a number is used to form an abbreviation.
For a given string word, a numeronym is a string with few or more contiguous letters between the first letter and last letter of word replaced with a number representing the count of letters omitted. Only one set of contiguous letters are replaced by a number.
e.g. “L10n” is called a numeronym of the word “Localization”, where 10 stands for the count of letters between the first
letter 'L' and the last letter 'n' in the word.

Example
Input: “nailed”

Output: ["n4d", "na3d", "n3ed", "n2led", "na2ed", "nai2d"]

“n4d” is an abbreviation of given string “nailed” where “aile” string letters are omitted and replaced by count of letters, i.e. 4.
“na3d” is an abbreviation of given string “nailed” where “ile” string letters are omitted and replaced by count of letters, i.e. 3.
And so on.
Notes
Input Format: Only one argument denoting input string word.
Output: Return strings array containing all possible numeronyms of given string word.  You don’t need to worry about the order of strings in your output array. For words = "aaaaa", arrays ["a2aa", "aa2a", "a3a"], ["a3a", "aa2a", "a2aa"] etc will be considered a valid answer. In case of no possible numeronym string, return empty list.

Constraints:
String will be composed of characters [a-z], [A-Z], [0-9] only.
1 <= n <= 120 where n is length of given string word.
"""

def neuronyms(word):
    result = []
    for i in range(1, len(word)):
        for j in range(i + 2, len(word)):
            prefix = word[:i]
            tmp = str(len(word[i:j]))
            surfix = word[j:]
            result.append(prefix + tmp + surfix)
    return result
word = "nailed"
print(neuronyms(word))