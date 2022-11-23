# 19. Task as above. Function returning whether king can reach from w,k field to any board corner.
# Solution: this time I call a recursive function four times considering each corner respectively. When the king will
# reach certain corner, I just return true value and false otherwise when there is no path to any board corner.


# function returning first digit of a given number
def first_digit(k):
    a = 0
    while k:
        a = k % 10
        k //= 10
    return a


# function checking whether last digit of a board[a1][b1] is smaller than first digit of board[a2][b2]
def can_move(board, a1, b1, a2, b2):
    return board[a1][b1] % 10 < first_digit(board[a2][b2])


# counting distance from board[x][y] to board[a][b]
# (a,b) represents one of board corners
def distance(a, b, x, y):
    return ((a-x)**2 + (b-y)**2) ** (1/2)


# recursive function
def ex18_reku(board, w, k, dist, moves, logic_board, a, b):
    logic_board[w][k] = 1
    if (w, k) == (a, b):
        return True
    for x, y in moves:
        if 0 <= w+x < len(board) and 0 <= k+y < len(board):
            if can_move(board, w, k, w+x, k+y) and distance(a, b, w+x, y+k) <= dist and logic_board[w+x][k+y] == 0:
                if ex18_reku(board, w+x, k+y, distance(a, b, w+x, y+k), moves, logic_board, a, b):
                    return True
    logic_board[w][k] = 0
    return False


# main function
def ex18(board, w, k):
    n = len(board)
    logic_board = [[0 for _ in range(n)] for _ in range(n)]
    moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    corners = [(0, 0), (n-1, 0), (0, n-1), (n-1, n-1)]
    for x, y in corners:
        basic_distance = distance(x, y, w, k)
        if ex18_reku(board, w, k, basic_distance, moves, logic_board, x, y):
            return True
    return False


board = [[30, 50, 49, 30, 49, 17, 39, 14],
         [33, 10, 50, 36, 26, 24, 34, 25],
         [19, 22, 9, 21, 47, 6, 19, 45],
         [15, 10, 42, 27, 21, 3, 20, 4],
         [7, 30, 6, 18, 13, 40, 46, 47],
         [21, 46, 50, 16, 10, 22, 32, 36],
         [11, 26, 43, 25, 24, 36, 24, 50],
         [40, 38, 40, 17, 36, 13, 38, 36]]
w, k = 3, 4
print(ex18(board, w, k))
