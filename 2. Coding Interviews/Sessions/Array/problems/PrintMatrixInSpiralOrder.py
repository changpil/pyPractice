"""
Given a character matrix, return all the characters in the clockwise spiral order starting from the top-left.
Example
Input:
[
['X' 'Y' 'A']
['M' 'B' 'C']
['P' 'Q' 'R']
]

Output: "XYACRQPMB"

For the given matrix rows = 3 and cols = 3. Spiral order is 'X' -> 'Y' -> 'A' -> 'C' -> 'R' -> 'Q' -> 'P' -> 'M' -> 'B'. So return string "XYACRQPMB" of length rows * cols = 9.

Notes
Input Parameters: There is only one argument denoting character matrix matrix.

Output: Return a string res, of length rows * cols denoting the spiral order of matrix.

Constraints:
1 <= rows, cols
1 <= rows * cols <= 10^5
Any character in matrix will be either uppercase letter ('A' - 'Z') or lowercase letter ('a' - 'z').
Avoid recursion.

This problem is less about logic, but more about careful index manipulation.
Hint - It may be faster to write this, if you name your variables clearly. Instead of i,j,k,l etc, try naming them like row, col, start, end etc. That will also help your interviewer follow along more easily.

Custom Input
Input Format: The first line of input should contain an integer rows, denoting no. of rows of matrix. Second line should contain an integer cols, denoting no. of columns of matrix. In next rows lines, ith line should contain cols space separated characters, where jth character in this iith line denotes character at matrix[i][j]. If row = 3, col = 3 and matrix = [ ['X' 'Y' 'A'], ['M' 'B' 'C'], ['P' 'Q' 'R'] ], then input should be:
3
3
X Y A
M B C
P Q R

Output Format: There will be one line of output, containing a string res, denoting the string value returned by solution function.
For input row = 3, col = 3 and matrix = [ ['X' 'Y' 'A'], ['M' 'B' 'C'], ['P' 'Q' 'R'] ], output will be: XYACRQPMB
.
.
.
.
.
Autocomplete
I/O
"""

def  printSpirally(matrix):
    sn, sm, ln, lm = 0, 0, len(matrix) - 1, len(matrix[0]) -1
    ranges = []
    while sn <= ln and sm <= lm:
        row1 = [range(sn, sm +1), range(sm, lm +1)]
        col2 = [range(sn + 1, ln + 1), range(lm, lm +1 )]
        row3 = [range(ln, ln+1), range(lm-1, sm-1, -1)]
        col4 = [range(ln-1,sn, -1), range(sm, sm +1)]
        ranges.append(row1)
        ranges.append(col2)
        ranges.append(row3)
        ranges.append(col4)
        sn += 1
        ln -= 1
        sm += 1
        lm -= 1
    result = []
    for range1, range2 in ranges:
        for row in range1:
            for col in range2:
                # print(row, col, matrix[row][col])
                result.append(matrix[row][col])
    return "".join(result)

# m = [['X','Y', 'A'], ['M', 'B', 'C'], ['P', 'Q', 'R']]
# for l in m:
#     print(l)
# print(printSpirally(m))
#
#
# m = [['X','Y', 'A', 'P'], ['M', 'B', 'C', 'Z'], ['P', 'Q', 'R', "Q"], ['9', 'F', "J", 'D']]
# for l in m:
#     print(l)
# print(printSpirally(m))




def  printSpirally(matrix):
    sn, sm, ln, lm = 0, 0, len(matrix) - 1, len(matrix[0]) -1
    result = []
    while sn <= ln and sm <= lm:
        j = sm
        while j <= lm and sn <= ln:
            result.append(matrix[sn][j])
            j += 1
        sn += 1
        i = sn
        while i <= ln and sm <= lm:
            result.append(matrix[i][lm])
            i += 1
        lm -= 1
        j = lm
        while j >= sm and sn <= ln:
            result.append(matrix[ln][j])
            j -= 1
        ln -= 1
        i = ln
        while i >= sn and sm <= lm:
            result.append(matrix[i][sm])
            i -= 1
        sm += 1
    return "".join(result)

# m = [['X','Y', 'A'], ['M', 'B', 'C'], ['P', 'Q', 'R']]
# for l in m:
#     print(l)
# print(printSpirally(m))
#
#
# m = [['X','Y', 'A', 'P'], ['M', 'B', 'C', 'Z'], ['P', 'Q', 'R', "Q"], ['9', 'F', "J", 'D']]
# for l in m:
#     print(l)
# print(printSpirally(m))


# m = [['a'], ['b']]
# for l in m:
#     print(l)
# print(printSpirally(m))


# Wrong
m = [['a', 'b']]
for l in m:
    print(l)
print(printSpirally(m))

#Wrong
m = [['a'], ['b'], ['c'], ['d'], ['e']]
for l in m:
    print(l)
print(printSpirally(m))