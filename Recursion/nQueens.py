"""
No two queens are in the same row and column or diagonal
Q is for queens placed and . is an empty place
"""

def nQueens(matrix):

    result = []
    for i in range(matrix):
        for j in range(matrix):
            board = [["." for _ in range(matrix)] for _ in range(matrix)]
            board[i][j] = "Q"
            _nQueens(board, 0, 0)
            result.append(board)
    import pprint
    pprint.pprint(result)

def _nQueens(board, i, j):
    if i >= len(board) or j >= len(board):
        return True

    if i < 0 or j < 0 :
        return True

    if _col(board, i, j) and _row(board, i, j) and _cross(board, i,j):
        board[i][j] = "Q"
    _nQueens(board, i+1, j)
    _nQueens(board, i , j + 1)
    _nQueens(board, i + 1, j + 1)

def _col(board, i,j):
    for col in range(len(board)):
        if board[col][j] == "Q":
            return False
    return True

def _row(board, i,j):
    for row in range(len(board)):
        if board[i][row] == "Q":
            return False
    return True


# Mistake by infinite loop:
#by return doing _cross(board, i + knapsack, j + knapsack )  and _cross(board, i -knapsack, j -knapsack)

def _cross(board, i, j, direction = None):
    if i < 0 or j < 0:
        return True

    if i >= len(board) or j >= len(board):
        return True

    if board[i][j] == "Q":
        return False

    result = True
    if direction == "+":
        result = _cross(board, i + 1, j + 1 , "+")
    elif direction == "-":
        result = _cross(board, i -1, j -1, "-")
    elif direction == None:
        result = _cross(board, i + 1, j + 1 , "+")  and _cross(board, i -1, j -1, "-")

    return result

nQueens(3)