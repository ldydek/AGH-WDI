# 4. We have a given 2d array with natural numbers. Write program, which returns row and column number of the element
# for which quotient of elements sum in a column by elements sum in a row is the biggest.
# Solution: In that array are only natural numbers, so we just have to determine index of the column with the biggest
# sum and index of the row with the lowest sum.
# r - row, c - column

def ex4(arr):
    n = len(arr)
    sum1, sum2 = 10**10, 0
    r, c = 0, 0
    for x in range(n):
        ctr = 0
        for y in range(n):
            ctr += arr[x][y]
        if ctr < sum1:
            sum1 = ctr
            r = x
    for x in range(n):
        ctr = 0
        for y in range(n):
            ctr += arr[y][x]
        if ctr > sum2:
            sum2 = ctr
            c = x
    return r, c


arr = [[1, 3, 4], [5, 1, 2], [1, 4, 60]]
print(ex4(arr))
