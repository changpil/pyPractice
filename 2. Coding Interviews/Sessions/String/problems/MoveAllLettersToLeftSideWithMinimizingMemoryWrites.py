"""
You are given a string s, which may contain alphabet letters ('a' - 'z' or 'A' - 'Z') as well as numerical characters ('0' - '9'), in random order. Numerical characters are garbage characters and we don't care about them. Inside the same string, you have to make all alphabet letters appear on the left side though in the same order they appeared originally. Suppose in our architecture, memory write is a very expensive operation, so we have to minimize the number of writes. As digits are garbage, we need not to move them on the right side. Here we can save some memory writes!

Example One
Input: “1x”
Output: “xx”
“xx” is the only correct answer. “x1”, for example, is a wrong answer since reaching that string would have required two memory writes while reaching “xx” requires one.

Example Two
Input: "0a193zbr"
Output: "azbr3zbr"
In the given string letters are a, z, b and r. We can move all four letters to the left side with 4 write operations and get the string "azbr3zbr". Reaching any other string would have taken more than four writes, so "azbr3zbr" is the only correct answer.
Notes
Input Parameters: Function has one argument, string s.
Output: Return a string after moving all alphabet characters to the left using the minimal number of memory writes.

Constraints:
1 <= length of s <= 10^5

An in-place linear solution is expected.
For languages that have immutable strings, convert the input string into a character array and work in-place on that array. Convert it back to the string before returning. Ignore the extra linear space used in that conversion, as long as you're only using constant space after conversion to a character array.

Custom Input
Input Format: The first and only line of input should contain a string s. If s = “0a193zbr”, then input should be:
0a193zbr

Output Format: There is only one line of output, containing a string res, denoting the string value returned by solution function. For input s = “0a193zbr”, output will be:
azbr3zbr
"""


def move_letters_to_left_side_with_minimizing_memory_writes(s):
    allLetters = -1
    i = 0
    ss = list(s)
    while i < len(s):
        if 'a' <= ss[i] <= 'z' or 'A' <= ss[i] <= 'Z': 
            allLetters += 1
            ss[allLetters] = ss[i]
        i += 1

    return "".join(ss)

s = "0a193zbr"

print(move_letters_to_left_side_with_minimizing_memory_writes(s))
