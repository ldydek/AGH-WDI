# 14. Write program computing cos(x) using Maclaurin series.
# Solution: In "maclaurin_series" function we compute an nth element of this sequence using factorial from the "math"
# module. Later, in main function when two contiguous elements values become almost the same we can just return sum of
# all elements encountered so far. That value (for certain "x") is approximately equal to cos(x).

from math import factorial


def maclaurin_series(x, n):
    return ((-1)**n)*(x**(2*n))/factorial(2*n)


def ex14(x):
    suma, a, b, ctr = 0, 0, 1, 0
    while abs(a-b) > 10**(-40):
        a, b = maclaurin_series(x, ctr), maclaurin_series(x, ctr+1)
        suma += a + b
        ctr += 2
    return suma


print(ex14(6.28))
