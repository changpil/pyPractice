"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
"""


def isLongPressedName(name, typed):
    return foo(name, 0, typed, 0)


def foo(name, i, typed, j):
    if i == len(name) and len(typed) == j:
        return True
    if len(name) != i and len(typed) == j:
        return False
    if len(name) == i and len(typed) != j:
        return False

    if name[i] != typed[j]:
        return False
    return foo(name, i + 1, typed, j + 1) or foo(name, i, typed, j + 1)