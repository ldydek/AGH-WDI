# 18. On a chessboard field with dimensions 8x8 there is a certain integer. We try to move a king from board[w][k] field
# to board[8][8], but there are several restrictions:
# 1) King has to stay on chessboard
# 2) King can only move to that field in which integer first digit is grater than integer last digit of a current field
# 3) King can't move to a field which has a bigger distance to destination than current field (in other words during
# king's moves distance to destination can't increase).
# Solution: from starting position I consider all 8 directions and checks task conditions. When I reach some field and
# can't move further I back to previous field and consider remaining directions (backtracking). Eventually, when king
# will be on board[8][8] it means that certain path truly exists. Otherwise, if I consider all possible paths (traverse
# entire recursion tree) and won't be at board[8][8] it means that appropriate path doesn't exist. Note that allocating
# additional matrix with binary values prevents from coming into infinity recursion, for instance, if three 21 numbers
# would be next to each other.

from random import randint


# function returning first digit of a given number
def first_digit(k):
    a = 0
    while k:
        a = k % 10
        k //= 10
    return a


# function checking whether last digit of a board[a1][b1] is smaller than first digit of board[a2][b2]
def can_move(board, a1, b1, a2, b2):
    if board[a1][b1] % 10 < first_digit(board[a2][b2]):
        return True


# counting distance from board[x][y] to board[8][8]
def distance(x, y):
    return ((8-x)**2 + (8-y)**2) ** (1/2)


# recursive function
def ex18_reku(board, w, k, dist, moves, logic_board):
    logic_board[w][k] = 1
    if (w, k) == (len(board)-1, len(board)-1):
        return True
    for x, y in moves:
        if 0 <= w+x < len(board) and 0 <= k+y < len(board):
            if can_move(board, w, k, w+x, k+y) and distance(w+x, y+k) <= dist and logic_board[w+x][k+y] == 0:
                if ex18_reku(board, w+x, k+y, distance(w+x, y+k), moves, logic_board):
                    return True
    logic_board[w][k] = 0


# main function
def ex18(board):
    n = len(board)
    basic_distance = distance(0, 0)
    logic_board = [[0 for _ in range(n)] for _ in range(n)]
    moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    if ex18_reku(board, 0, 0, basic_distance, moves, logic_board) is True:
        return True
    return False


board = [[randint(1, 50) for _ in range(8)] for i in range(8)]
print(ex18(board))
