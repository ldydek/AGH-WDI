# 12. Write program printing greatest common divisor (GCD) of three given numbers.
# Solution: We can compute GCD of two numbers using Euclidean algorithm and later compute GCD once again for GCD
# of "a" and "b" and for remaining value "c". Note that expression min(gcd(a, b), gcd(a, c), gcd(b, c) doesn't always
# compute correct GCD of three numbers e.g. for (10, 12, 15) GCD is 1 and min(gcd(10, 12), gcd(12, 15), gcd(10, 15)) is
# 2. That way is correct: gcd(10, 12, 15) = gcd(gcd(10, 12), 15) = gcd(2, 15) = 1.

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def ex12(a, b, c):
    return gcd(gcd(a, b), c)
