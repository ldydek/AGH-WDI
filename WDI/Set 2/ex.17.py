# 17. Solve equation x^x = 2020 using Newton's method (tangent method).
# Solution: using derivative of function f (f(x) = x^2 - 2020) I struggle to come as close as possible to the solution
# that is within our epsilon (here 10^(-2)).

from math import log
from math import e


def derivative(x):
    return (e ** (x * log(x, e))) * (1 + log(x, e))


def f(x):
    return x ** x - 2020


def ex17():
    x = 4
    while abs(f(x)) > 10 ** (-2):
        x -= f(x)/derivative(x)
    return x


print(ex17())
