# 12. Write program printing greatest common divisor (GCD) of three given numbers.
# Solution: We can compute GCD of two numbers using Euclidean algorithm.

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def ex12(a, b, c):
    return gcd(gcd(a, b), c)
