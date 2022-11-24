# 01. Rational numbers are represented by tuple (l,m), where "l" is an integer representing numerator and
# "m" denominator. Write basic functions on fractions for instance adding, subtracting, multiplying, division,
# exponentiation, shortening, printing and loading.


# function adding two fractions
def addition(a, b):
    return shortening((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))


# function subtracting two fractions
def subtraction(a, b):
    return shortening((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))


# function multiplying two fractions
def multiplication(a, b):
    return shortening((a[0] * b[0], a[1] * b[1]))


# function dividing fraction "a" by fraction "b"
def division(a, b):
    return shortening((a[0] * b[1], a[1] * b[0]))


# function raising a number to a nth power
def power(a, n):
    return shortening((a[0] ** n, a[1] ** n))


# function checking whether two fractions are equal
def equal(a, b):
    return a[0] * b[1] == a[1] * b[0]


# function returning greatest common divisor of two integers
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# function shortening certain fraction
def shortening(a):
    g_c_d = gcd(a[0], a[1])
    return a[0]//g_c_d, a[1]//g_c_d


# enter numbers separated by / e.g. 2/3
def fraction_input():
    l, m = input().split("/")
    l = int(l)
    m = int(m)
    return l, m


def ex01():
    l1, m1 = fraction_input()
    l2, m2 = fraction_input()
    print(addition((l1, m1), (l2, m2)))
    print(subtraction((l1, m1), (l2, m2)))
    print(multiplication((l1, m1), (l2, m2)))
    print(division((l1, m1), (l2, m2)))
    print(power((l1, m1), 3))
    print(equal((l1, m1), (l2, m2)))
    print(shortening((l1, m1)))


ex01()
