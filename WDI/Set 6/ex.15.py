# 15. 8 queens problem (obvious content).
# Solution: using backtracking we can easily solve this problem. At the beginning, I place first queen on board[0][0],
# so first column is already occupied. Now we want to put somewhere second queen. So we traverse second column and look
# for first field that is safe. The same idea goes to remaining quantity of queens. Unfortunately, during that algorithm
# we won't be able later to put somewhere certain queen. That's when backtracking comes. We back using recursion to
# previous queen and change its position. After this action we check if placing next queen is possible. At the end, we
# will consider lots of possibilities of placing 8 queens and eventually function returns possible placing of them.

# function checking if I can put queen on board[i][j]
def safe(board, i, j):
    n = len(board)
    # row and column
    for x in range(n):
        if board[i][x] == 1 or board[x][j] == 1:
            return False
    ctr1, ctr2 = 0, 0

    # first diagonal
    while i+ctr1 < n and j+ctr2 < n:
        if board[i+ctr1][j+ctr2] == 1:
            return False
        ctr1 += 1
        ctr2 += 1
    ctr1, ctr2 = 0, 0
    while 0 <= i+ctr1 and 0 <= j+ctr2:
        if board[i+ctr1][j+ctr2] == 1:
            return False
        ctr1 -= 1
        ctr2 -= 1

    # second diagonal
    ctr1, ctr2 = 0, 0
    while 0 <= i+ctr1 < n and 0 <= j+ctr2 < n:
        if board[i+ctr1][j+ctr2] == 1:
            return False
        ctr1 -= 1
        ctr2 += 1
    ctr1, ctr2 = 0, 0
    while 0 <= i + ctr1 < n and 0 <= j + ctr2 < n:
        if board[i + ctr1][j + ctr2] == 1:
            return False
        ctr1 += 1
        ctr2 -= 1
    return True


def eight_queens_problem(board, col):
    n = len(board)
    if col == n:
        return True
    for x in range(n):
        if safe(board, x, col):
            board[x][col] = 1
            if eight_queens_problem(board, col+1):
                return board
            board[x][col] = 0
    return False


def ex15(board):
    return eight_queens_problem(board, 0)


board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
print(ex15(board))
