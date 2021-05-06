"""
Karat does not have limited questions. As you solve the questions, you will be asked to another questions.
in general, you need to solve more than 2. 5 to 3.
"""

"""
Design q1) how would you search direct friends?
user: userid, name, createdate
friends: friendid, user1, user2, createddate
"""

"""
Design q2) multiple users can use a document. one server can serve  a document.
If we loadBalacing by this, what is the problem?
1. Hot Spot.
2. rehasing problem
"""
"""
Coding Question 1
If grid has unique numbers 1 to n.

"""


# Time O(N^2)
# Space O(N)
def foo(grid):
    for i in range(len(grid)):
        row = [0] * len(grid)
        for j in range(len(grid[0])):
            if 1 <= grid[i][j] <= len(grid):
                if row[grid[i][j] - 1] != 0:
                    return False
                row[grid[i][j] - 1] = 1
            else:
                return False
    for j in range(len(grid[0])):
        col = [0] * len(grid)
        for i in range(len(grid)):
            if 1 <= grid[i][j] <= len(grid):
                if col[grid[i][j] - 1] != 0:
                    return False
                col[grid[i][j] - 1] = 1
            else:
                return False
    return True
print("#"*10, "coding Question 1", "#"*10)

"""
Coding question 2
A nonogram is a logic puzzle, similar to a crossword, in which the player is given a blank grid and has to color it according to some instructions. Specifically, each cell can be either black or white, which we will represent as 'B' for black and 'W' for white.

+------------+
| W  W  W  W |
| B  W  W  W |
| B  W  B  B |
| W  W  B  W |
| B  B  W  W |
+------------+

For each row and column, the instructions give the lengths of contiguous runs of black ('B') cells. For example, the instructions for one row of [ 2, 1 ] indicate that there must be a run of two black cells, followed later by another run of one black cell, and the rest of the row filled with white cells.

These are valid solutions: [ W, B, B, W, B ] and [ B, B, W, W, B ] and also [ B, B, W, B, W ]
This is not valid: [ W, B, W, B, B ] since the runs are not in the correct order.
This is not valid: [ W, B, B, B, W ] since the two runs of Bs are not separated by Ws.

Your job is to write a function to validate a possible solution against a set of instructions. Given a 2D matrix representing a player's solution; and instructions for each row along with additional instructions for each column; return True or False according to whether both sets of instructions match.

Example instructions #1

matrix1 = [[ W, W, W, W ],
           [ B, W, W, W ],
           [ B, W, B, B ],
           [ W, W, B, W ],
           [ B, B, W, W ]]
rows1_1    =  [], [1], [1,2], [1], [2]
columns1_1 =  [2,1], [1], [2], [1]
validateNonogram(matrix1, rows1_1, columns1_1) => True

Example solution matrix:
matrix1 ->
                                   row
                +------------+     instructions
                | W  W  W  W | <-- []
                | B  W  W  W | <-- [1]
                | B  W  B  B | <-- [1,2]
                | W  W  B  W | <-- [1]
                | B  B  W  W | <-- [2]
                +------------+
                  ^  ^  ^  ^
                  |  |  |  |
  column       [2,1] | [2] |
  instructions      [1]   [1]


Example instructions #2

(same matrix as above)
rows1_2    =  [], [], [1], [1], [1,1]
columns1_2 =  [2], [1], [2], [1]
validateNonogram(matrix1, rows1_2, columns1_2) => False

The second and third rows and the first column do not match their respective instructions.

Example instructions #3

(same matrix as above)
rows1_3    = [], [1], [3], [1], [2]
columns1_3 = [3], [1], [2], [1]
validateNonogram(matrix1, rows1_3, columns1_3) => False

The third row and the first column do not match their respective instructions.

Example instructions #4

matrix2 = [
 [ W, W ],
 [ B, B ],
 [ B, B ],
 [ W, B ]
]
rows2_1    = [], [2], [2], [1]
columns2_1 = [1, 1], [3]
validateNonogram(matrix2, rows2_1, columns2_1) => False

The black cells in the first column are not separated by white cells.

"""
# Time O(MN)
# Space O(M/N)
def foo(grid, rows, cols):
    for i in range(len(grid)):
        row_v = []
        bc = 0
        for j in range(len(grid[0])):
            if grid[i][j] == "B":
                bc += 1
            else:
                if bc != 0:
                    row_v.append(bc)
                    bc = 0
        if bc != 0:
            row_v.append(bc)
        if rows[i] != row_v:
            return False

    for j in range(len(grid[0])):
        col_v = []
        bc = 0
        for i in range(len(grid)):
            if grid[i][j] == "B":
                bc += 1
            else:
                if bc != 0:
                    col_v.append(bc)
                    bc = 0
        if bc != 0:
            col_v.append(bc)

        if cols[j] != col_v:
            return False
    return True

print("#"*10, "coding Question 2", "#"*10)
matrix1 = [
    ['W', 'W', 'W', 'W'],
    ['B', 'W', 'W', 'W'],
    ['B', 'W', 'B', 'B'],
    ['W', 'W', 'B', 'W'],
    ['B', 'B', 'W', 'W']
]
rows1_1 = [[], [1], [1, 2], [1], [2]]
columns1_1 = [[2, 1], [1], [2], [1]]

print(foo(matrix1, rows1_1, columns1_1))

rows1_2 = [[], [], [1], [1], [1, 1]]
columns1_2 = [[2], [1], [2], [1]]
print(foo(matrix1, rows1_2, columns1_2))

rows1_3 = [[], [1], [3], [1], [2]]
columns1_3 = [[3], [1], [2], [1]]

print(foo(matrix1, rows1_3, columns1_3))

matrix2 = [
    ['W', 'W'],
    ['B', 'B'],
    ['B', 'B'],
    ['W', 'B']
]

rows2_1 = [[], [2], [2], [1]]
columns2_1 = [[2], [3]]

print(foo(matrix2, rows2_1, columns2_1))

"""
# No time to solve this problem
Coding Question 3
Suppose you have a one-dimensional board of two colors of tiles. Red tiles can only move to the right, black tiles can only move to the left. 
A tile can move 1 space at a time. Either they move to an adjacent empty space, or they can jump over a single tile of the other color to an empty space.

Eg:
red = R
black = B
empty = _

R _ B _ => _ R B _ or
         R B _ _

R B _ _ => _ B R _

Given a start and end configuration represented as a list of strings, return a list of valid moves to get from start to end (doesn't need to be shortest), or None if none exist. 
Include the start and end states in the list of moves.

Example:
start = ['R', '_', 'B', 'B']
end = ['B', '_', 'B', 'R']
->
moves = [
  ['R', '_', 'B', 'B'],
  ['_', 'R', 'B', 'B'],
  ['B', 'R', '_', 'B'],
  ['B', 'R', 'B', '_'],
  ['B', '_', 'B', 'R']
]

"""


def drive(start, finish):
    if start.count("_") == 0:
            return None
    if start == finish:
        return [start, finish]
    tmp = []
    visited = set()
    tmp.append(start.copy())
    if _drive(start, finish, visited, tmp):
        return tmp
    else:
        return None

def _drive(start, finish,visited, tmp):
    if start == finish:
        return True
    #print(start)
    if tuple(start) in visited:
        return None

    visited.add(tuple(start))
    for i in range(len(start)):
        if start[i] == "R":
            if i + 1 < len(start) and start[i+1] == "_":
                start[i], start[i+1] = start[i+1], start[i]
                tmp.append(start.copy())
                if tuple(start) not in visited:
                    if _drive(start, finish, visited, tmp):
                        return True
                start[i + 1], start[i] = start[i], start[i + 1]
                tmp.pop()
            elif i + 2 < len(start) and start[i+1] == "B" and start[i+2] == "_":
                start[i], start[i+2] = start[i+2], start[i]
                tmp.append(start.copy())
                if tuple(start) not in visited:
                    if _drive(start, finish, visited, tmp):
                        return True
                start[i + 2], start[i] = start[i], start[i + 2]
                tmp.pop()
        elif start[i] == "B":
            if i - 1 >= 0 and start[i-1] == "_":
                start[i -1], start[i] = start[i], start[i-1]
                tmp.append(start.copy())
                if tuple(start) not in visited:
                    if _drive(start, finish, visited, tmp):
                        return True
                start[i - 1], start[i] = start[i], start[i - 1]
                tmp.pop()
            elif i + 2 >= 0 and start[i-1] == "R" and start[i-2] == "_":
                start[i], start[i-2] = start[i-2], start[i]
                tmp.append(start.copy())
                if tuple(start) not in visited:
                    if _drive(start, finish, visited, tmp):
                        return True
                start[i - 2], start[i] = start[i], start[i - 2]
                tmp.pop()
    visited.discard(tuple(start))
print("#"*10, "coding Question 3", "#"*10)
start = ["R", "_", "B", "B"]
finish = ["B", "_", "B", "R"]
print(drive(start, finish))




