"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
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
#b =[[".","8","7","6","5","4","3","2","Pattern1:knapsack"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
b= [["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","Pattern1:knapsack",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

s = Solution()
print(s.isValidSudoku(b))