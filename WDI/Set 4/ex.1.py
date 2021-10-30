# 1. There is given 2d array. Write program which completes it consecutive natural numbers in a spiral.


def ex1(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    ctr, a, b = 1, 0, n-1
    while a < b:
        for x in range(a, b):
            arr[a][x] = ctr
            ctr += 1
        for x in range(a, b):
            arr[x][b] = ctr
            ctr += 1
        for x in range(b, a, -1):
            arr[b][x] = ctr
            ctr += 1
        for x in range(b, a, -1):
            arr[x][a] = ctr
            ctr += 1
        a += 1
        b -= 1
    arr[a][b] = ctr
    return arr


print(ex1(5))

