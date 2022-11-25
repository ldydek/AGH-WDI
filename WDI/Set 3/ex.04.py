# 04. Write a program computing and printing "e" constant from a series e = 1/0! + 1/1! + 1/2! + 1/3! + ... with the
# accuracy to the "n" decimal digits ("n" is smaller or equal to 1000).
# Solution: I use here additional imported module which during dividing makes an accuracy to the given number.

import decimal


# function computing factorial of a given number
def factorial(n):
    value = 1
    for x in range(1, n+1):
        value *= x
    return value


# main function
def ex04(n):
    decimal.getcontext().prec = n + 1
    e = 0
    for x in range(1000):
        e += decimal.Decimal(1/factorial(x))
    return e


print(ex04(10))
