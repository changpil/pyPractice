"""
Given a string s containing a set of words, transform it such that the words appear in the reverse order. Words in s are separated by one or more spaces.

Example One
Input: “I will do it.”
Output: “it. do will I”

Example Two
Input: "   word1  word2 " (Note: there are 3 spaces in the beginning, 2 spaces between the words and 1 space at the end.)

Output: " word2  word1   " (Note: there is 1 space in the beginning, 2 spaces between the words and 3 spaces at the end.)

Example Three
Input: "word1, word2;"
Output: "word2; word1,"
Notes
Input Parameters: Function one argument, string s.
Output: Return a string with the answer.

Constraints:
1 <= length of s <= 10^5
s contains only lowercase and uppercase alphabetical characters, spaces and punctuation marks ".,?!':;-" (quotes not included).
"""

# Wrong Answer
def reverse_ordering_of_words(s):
    return " ".join(s.split()[::-1])

# w = "Hello World chang"
# print(reverse_ordering_of_words(w))


def reverse_ordering_of_words(s):
    ss = list(s)
    swap(ss, 0, len(ss)-1)
    i, j = 0, 0
    while i < len(ss):
        if ss[i] != " ":
            j = i + 1
            while j < len(ss) and ss[j] != " ":
                j += 1
            swap(ss, i, j -1)
            i = j + 1
        else:
            i += 1
    return "".join(ss)

def swap (ss, i, j):
    while i < j:
        ss[i], ss[j] = ss[j], ss[i]
        i += 1
        j -= 1


w = " Hello World chang  "
print(reverse_ordering_of_words(w))


# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()
# Chang
# Test Cases
# 1. "  " --> "  "
# 2. "a b c" --> "c b a"
# 3. "__a__b_c_" --> "_c_b__a__"
# 4. "__a_b_c"  --> "c_", "b_", "a__"

import collections
def reverse(s):
    stack = collections.deque()
    start, i = 0, 0
    isspace = False
    while i < len(s):
        if s[i] == " ":
            isspace = True
        if isspace and s[i] != " ":
            stack.append(s[start: i])
            start = i
            isspace = False
        i += 1

    stack.append(s[start:])
    print(stack)
    result = []
    while stack:
        t = foo(stack.pop())
        result.append(t)
    print(result)
    return "".join(result)


def foo(s):
    if s == "" or s[-1] != " ":
        return s
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    return s[i+1:] + s[:i+1 ]


#"__a_b_c"  --> "c", "b_", "a_", "__"
#       s
#        i


def reverse2(s):
    stack = []
    i = 0
    while i < len(s):
        start = i
        while i < len(s) and s[i] == " ":
            i += 1
        stack.append(s[start: i])
        start = i

        while i < len(s) and s[i] != " ":
            i += 1
        stack.append(s[start: i])
    print(stack)
    result = []
    while stack:
        t = stack.pop()
        result.append(t)
    print(result)
    return "".join(result)

w = "a  b  c"
print(reverse2(w))

w = " abc  d  gzzzz "
print(reverse2(w))


w = " a  b  c "
print(reverse2(w))

w = " abc  d  gzzzz sa"
print(reverse2(w))

