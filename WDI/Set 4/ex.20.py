# 20. There is given array T[N][N] (representing chessboard) filled with integers. Write function which sets a position
# for two rooks in which sum of all checked fields by these two rooks is the biggest. Assume that rook checks entire
# row and column except for a place on which it stands.
# Solution: at the beginning, an additional function computes sum of respective rows and columns and keeps that
# information in auxiliary arrays. In the main function we consider only this case in which two rooks are in different
# rows and columns, because never a situation where they have common row or column will be optimal (integers on
# chessboard).

def row_column_sum(T):
    n = len(T)
    rows = [0] * n
    columns = [0] * n
    for x in range(n):
        value = 0
        for y in range(n):
            value += T[x][y]
        rows[x] = value
    for x in range(n):
        value = 0
        for y in range(n):
            value += T[y][x]
        columns[x] = value
    return rows, columns


def chess(T):
    n = len(T)
    rows, columns = row_column_sum(T)
    solution = None
    value = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if a == c or b == d:
                        continue
                    elif a != c and b != d and value < rows[a] + rows[c] + columns[b] + columns[d] - 2*(T[a][b] + T[c][d]) - T[a][d] - T[c][b]:
                        value = rows[a] + rows[c] + columns[b] + columns[d] - 2*(T[a][b] + T[c][d]) - T[a][d] - T[c][b]
                        solution = [(a, b), (c, d)]
                    # different rows and columns
    return solution


T = [[1, 1, 2, 3], [-1, 3, -1, 4], [4, 1, 5, 4], [5, 0, 3, 6]]
print(chess(T))
