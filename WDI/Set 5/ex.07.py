# 07. Using functions from previous exercise write a function solving quadratic equation with complex coefficients.

from math import cos, sin, acos, pi


# enter complex number by typing x y which means x+yi
def complex_number_input():
    re, im = input().split(" ")
    re = int(re)
    im = int(im)
    return re, im


def addition(a, b):
    return a[0] + b[0], a[1] + b[1]


def multiplication(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def subtraction(a, b):
    return a[0] - b[0], a[1] - b[1]


def division(a, b):
    return ((a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2),
            (a[1] * b[0] - a[0] * b[1]) / (b[0] ** 2 + b[1] ** 2))


# using De Moivre's formula
def power(a, n):
    z = (a[0] ** 2 + a[1] ** 2) ** (1/2)
    cosx = a[0] / z
    ctr = 0
    if a[0] >= 0 and a[1] >= 0:
        ctr = 0
    elif a[0] < 0 <= a[1]:
        ctr = 1
    elif a[0] < 0 and a[1] < 0:
        ctr = 2
    elif a[0] >= 0 > a[1]:
        ctr = 3
    angle = acos(cosx) + ctr * (pi/2)
    return round((z ** n) * cos(angle * n)), round((z ** n) * sin(angle * n))


def ex07():
    a1, a2 = complex_number_input()
    b1, b2 = complex_number_input()
    c1, c2 = complex_number_input()
    # starting computing square root of discriminant here
    a = multiplication((b1, b2), (b1, b2))
    b = multiplication((a1, a2), (c1, c2))
    b = (b[0]*4, b[1]*4)
    discriminant = subtraction(a, b)
    discriminant = power(discriminant, 1/2)
    # ending computing square root of discriminant
    b1, b2 = multiplication((b1, b2), (-1, 0))
    x1 = division(addition((b1, b2), discriminant), (2, 0))
    x2 = division(subtraction((b1, b2), discriminant), (2, 0))
    return x1, x2


print(ex07())
