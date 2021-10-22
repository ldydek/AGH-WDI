# 14. Write program computing cos(x) using Maclaurin series.
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
