# 5. The same problem as in exercise 4, but this time array contains integer numbers.
# Solution: Sum of the row or column elements can be negative, so we have to additionally check, whether this quotient
# will be bigger than this one with positive integers.
# a - column index with the biggest positive sum
# b - row index with the smallest positive sum
# c - column index with the smallest negative sum
# d - row index with the biggest negative sum
# Note that situation with e.g. each sum of column elements is positive and each sum of row elements is negative can't
# happen, because in that case sum of all elements in the matrix had to be positive and negative at once, so one of
# these two fractions (a/b or c/d) is correctly determined. There is only one pessimistic case, when all elements are
# 0 and then program informs us printing "False".

def ex5(arr):
    n = len(arr)
    a, b, c, d = 0, 0, 0, 0
    sum1, sum2, sum3, sum4 = 0, 10**15, 0, -10**15

    for x in range(n):
        ctr = 0
        for y in range(n):
            ctr += arr[x][y]
        if 0 < ctr < sum2:
            sum2 = ctr
            b = x
        elif 0 > ctr > sum4:
            sum4 = ctr
            d = x

    for x in range(n):
        ctr = 0
        for y in range(n):
            ctr += arr[y][x]
        if ctr > sum1:
            sum1 = ctr
            a = x
        elif ctr < sum3:
            sum3 = ctr
            c = x

    if sum1 == sum3 == 0:
        return False
    elif sum1/sum2 > sum3/sum4:
        return b, a, sum1/sum2
    return d, c


arr = [[-2, 10, -9], [-10, 5, 3], [5, 1, -90]]
print(ex5(arr))
