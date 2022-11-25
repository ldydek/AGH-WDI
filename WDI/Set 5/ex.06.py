# 06. Complex numbers are represented by a tuple (re, im), where re - real part number, im - imaginary part number.
# Write basic operations on that kind of numbers, for instance, adding, subtracting, multiplying, division,
# exponentiation, printing, loading.

from math import sin, cos, acos, pi


def addition(a, b):
    return a[0] + b[0], a[1] + b[1]


def subtraction(a, b):
    return a[0] - b[0], a[1] - b[1]


def multiplication(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


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


def printing(n):
    print("(" + str(n[0]) + ")" + "+" + "(" + str(n[1]) + "i)")


# enter complex number by typing x y which means x+yi
def complex_number_input():
    re, im = input().split(" ")
    re = int(re)
    im = int(im)
    return re, im


def ex06():
    re1, im1 = complex_number_input()
    re2, im2 = complex_number_input()
    printing((re1, im1))
    print(addition((re1, im1), (re2, im2)))
    print(subtraction((re1, im1), (re2, im2)))
    print(multiplication((re1, im1), (re2, im2)))
    print(division((re1, im1), (re2, im2)))
    print(power((re1, im1), 10))


ex06()
