"""
Zigzag A Word
A word can be written in a vertical zigzag fashion in a given number of lines, e.g. KICKSTART in three lines looks like this:
K        S        T
I    K   T   R
C        A
Reading this text line by line gives us KSTIKTRCA.
Given a word and a number of lines for zigzagging, return that line-by-line representation.
Example One
{
"nlines": 4,
"word": "INTERVIEW"
}
Output:
"IINVETRWE"
Because zigzagging INTERVIEW in four lines gives this:
I                    I
N          V     E
T    R           W
E
Example Two
{
"nlines": 1,
"word": "KICKSTART"
}
Output:
"KICKSTART"
Notes
Constraints:
1 <= word length <= 100000
1 <= number of lines <= 100000
Word consists of characters a..z, A..Z, 0..9
"""

def zigzag(nlines, word):
    if nlines == 1:
        return word
    lines = [[] for _ in range(nlines) ]
    reversed = True
    for i in range(len(word)):
        if i%(nlines-1) == 0:
            reversed = not reversed
        if not reversed:
            lines[i%(nlines-1)].append(word[i])
        else:
            lines[(nlines-1) - i%(nlines-1)].append(word[i])

    result = ""
    for l in lines:
        print(l)
    for l in lines:
         result += "".join(l)

    return result


word = "Helloworld"
print(zigzag(2, word))

word = "Helloworld"
print(zigzag(3, word))


word = "Helloworld"
print(zigzag(4, word))