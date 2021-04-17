"""
https://leetcode.com/problems/snakes-and-ladders/
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations, regardless of the size of the board.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.

"""
import collections
def snakesAndLadders(board):
    q = collections.deque()
    q.append(1)
    steps = 0
    visited = set()
    while q:
        level = len(q)
        for _ in range(level):
            num = q.popleft()
            if num == len(board)*len(board[0]):
                return steps
            for next_num in getNeighbors(board, num, visited):
                q.append(next_num)
        steps += 1
    return -1

def getNeighbors(board, num, visited):
    neighbors = [num+1, num+2, num +3, num+ 4, num+5, num +6]
    for neighbor in neighbors:
        i, j = getPoint(board, neighbor)
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            continue
        if neighbor in visited:
            continue
        visited.add(neighbor)
        if board[i][j] != -1:
            yield board[i][j]
        else:
            yield neighbor

def getPoint(board, num):
    forward = (len(board) -1) % 2
    num -= 1
    row = len(board) - 1 - num//(len(board))
    if row %2 == forward:
        col = (num) %len(board)
    else:
        col = len(board[0]) -1  - num%(len(board))
    return row, col

# board = [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]

# Test numToIndex Convertion
#board = [[0]*10 for _ in range(10)]
# for i in range(1, 30):
#     print(i, getPoint(board,i))

#print(snakesAndLadders(board))


# Infinite Loop
# board = [[1,1,-1],[1,1,1],[-1,1,1]]
# print(snakesAndLadders(board))

# Time Limit Exceeded
board = [[-1,-1,-1,135,-1,-1,-1,-1,-1,185,-1,-1,-1,-1,105,-1],
         [-1,-1,92,-1,-1,-1,-1,-1,-1,201,-1,118,-1,-1,183,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1,-1,179,-1,-1,-1,-1,-1,-1],
         [-1,248,-1,-1,-1,-1,-1,-1,-1,119,-1,-1,-1,-1,-1,192],
         [-1,-1,104,-1,-1,-1,-1,-1,-1,-1,165,-1,-1,206,104,-1],
         [145,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,229,-1],
         [-1,-1,75,140,-1,-1,-1,-1,-1,-1,-1,-1,43,-1,34,-1],
         [-1,-1,-1,-1,-1,-1,169,-1,-1,-1,-1,-1,-1,188,-1,-1],
         [-1,-1,-1,-1,-1,-1,92,-1,171,-1,-1,-1,-1,-1,-1,66],
         [-1,-1,-1,126,-1,-1,68,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,109,-1,86,28,228,-1,-1,144,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,59,-1,-1,-1,-1,-1,51,-1,-1,-1,62,-1],
         [-1,71,-1,-1,-1,63,-1,-1,-1,-1,-1,-1,212,-1,-1,-1],
         [-1,-1,-1,-1,174,-1,59,-1,-1,-1,-1,-1,-1,133,-1,-1],
         [-1,-1,62,-1,5,-1,16,-1,-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,59,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
print(snakesAndLadders(board))
