# Solution: at the beginning, an additional function computes sum of respective rows and columns and keeps that
# information in auxiliary arrays. In the main function we consider every possible position of two rooks and depending
# on it I take sum of certain row or column once or twice (for instance, if rooks are in the same row then only once).
# If counted sum is greater then current sum I changed this value and the best position of two rooks found so far.
# Passed all tests.

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
    # now let's consider every possible position of two rooks in a matrix
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if a == c and b == d:
                        continue
                    # rooks can't be in the same place on the chessboard
                    elif a == c and value < rows[a] + columns[b] + columns[d] - 2*(T[a][b] + T[c][d]):
                        value = rows[a] + columns[b] + columns[d] - 2*(T[a][b] + T[c][d])
                        solution = [(a, b), (c, d)]
                    # the same row
                    elif b == d and value < rows[a] + rows[c] + columns[b] - 2*(T[a][b] + T[c][d]):
                        value = rows[a] + rows[c] + columns[b] - 2*(T[a][b] + T[c][d])
                        solution = [(a, b), (c, d)]
                    # the same column
                    elif a != c and b != d and value < rows[a] + rows[c] + columns[b] + columns[d] - 2*(T[a][b] + T[c][d]) - T[a][d] - T[c][b]:
                        value = rows[a] + rows[c] + columns[b] + columns[d] - 2*(T[a][b] + T[c][d]) - T[a][d] - T[c][b]
                        solution = [(a, b), (c, d)]
                    # different rows and columns (the most possible case)
    return solution


T = [[1, 1, 2, 3], [-1, 3, -1, 4], [4, 1, 5, 4], [5, 0, 3, 6]]
print(chess(T))
