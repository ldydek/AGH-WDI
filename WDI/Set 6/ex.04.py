# 4. Chess knight problem. Write program completing a chessboard with consecutive natural numbers by knight's move.
# Solution: I can write possible moves by knight in a "moves" array. In the recursive function I am on a certain
# position (at the beginning e.g. arr[0][0]) and if I can move to suitable place I do it (suitable place means free
# place on a chessboard, which wasn't visited so far). Assigning 0 to arr[x][y] is pivotal in this program, because
# if there will be possibility when knight can't move anywhere but chessboard is still not completed, we recursively
# return to the previous situation (leaving this location free) and from that place we try another direction. At the
# end, if counter will be equal to array length to the second power, it means we found a solution. Note that the
# solution is not unique in general.


def ex4(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
    ex4_recu(arr, moves, 0, 0, 1)
    for x in range(n):
        for y in range(n):
            print(arr[x][y], end="  ")
        print()


def ex4_recu(arr, moves, x, y, ctr):
    arr[x][y] = ctr
    if ctr == len(arr) ** 2:
        return True
    for i in range(len(moves)):
        if 0 <= x + moves[i][0] <= len(arr)-1 and 0 <= y + moves[i][1] <= len(arr)-1:
            if arr[x+moves[i][0]][y+moves[i][1]] == 0:
                value = ex4_recu(arr, moves, x+moves[i][0], y+moves[i][1], ctr+1)
                if value:
                    return True
    arr[x][y] = 0


ex4(5)
