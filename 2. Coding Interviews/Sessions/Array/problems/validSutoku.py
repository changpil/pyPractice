"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


class Solution:
    def isValidSudoku(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].isdigit() and not self.check(board, i, j):
                    return False
        return True

    def check(self, board, row, col):
        return self.check_row(board, row, col) and self.check_col(board, row, col) and self.check_block(board, row, col)

    def check_row(self, board, row, col):
        target = board[row][col]
        for i in range(len(board)):
            if i != row and target == board[i][col]:
                return False
        return True

    def check_col(self, board, row, col):
        target = board[row][col]
        for i in range(len(board[row])):
            if i != col and target == board[row][i]:
                return False
        return True

    def check_block(self, board, row, col):
        col_range = col // 3
        row_range = row // 3
        target = board[row][col]
        dic = {0: range(0, 3), 1: range(3, 6), 2: range(6, 9)}
        for i in dic[row_range]:
            for j in dic[col_range]:
                if (i != row or j != col) and target == board[i][j]:
                    return False
        return True


grid = [[".",".",".","1","4",".",".","2","."],
         [".",".","6",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".","1",".",".",".",".",".","."],
         [".","6","7",".",".",".",".",".","9"],
         [".",".",".",".",".",".","8","1","."],
         [".","3",".",".",".",".",".",".","6"],
         [".",".",".",".",".","7",".",".","."],
         [".",".",".","5",".",".",".","7","."]]
s = Solution()
print(s.isValidSudoku(grid))

def sudoku2(grid):
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ".":
                continue
            if grid[i][j] in visited:
                return False
            else:
                visited.add(grid[i][j])
        visited.clear()
    visited.clear()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[j][i] == "." :
                continue
            if grid[j][i] in visited:
                return False
            else:
                visited.add(grid[j][i])
        visited.clear()
    visited.clear()
    for row in range(0, len(grid), 3):
        for col in range(0, len(grid), 3):
            for i in range(row, row + 3):
                for j in range(col, col+3):
                    if grid[i][j] == ".":
                        continue
                    if grid[i][j] in visited:
                        return False
                    else:
                        visited.add(grid[i][j])
            visited.clear()
    return True
grid = [[".",".",".","1","4",".",".","2","."],
         [".",".","6",".",".",".",".",".","."],
         [".",".",".",".    ",".",".",".",".","."],
         [".",".","1",".",".",".",".",".","."],
         [".","6","7",".",".",".",".",".","9"],
         [".",".",".",".",".",".","8","1","."],
         [".","3",".",".",".",".",".",".","6"],
         [".",".",".",".",".","7",".",".","."],
         [".",".",".","5",".",".",".","7","."]]

print(sudoku2(grid))