# 20. Write program computing the lowest number system base for which given numbers don't have common digit.
# For example, for numbers 123 and 522 the answer is 11, because for that number system we have 123(10) = 102(11) and
# 522(10) = 435(11) and if we represent these numbers in a smaller base of number system they'll have at least one
# common digit. If this base doesn't exist program should return "False". Note that we could use array as well for
# checking common digits of two numbers, but below is an approach without using it.


def change_system(n, a):
    number = ""
    while n:
        if n % a < 10:
            number += str(n % a)
        else:
            if n % a == 10:
                number += "A"
            elif n % a == 11:
                number += "B"
            elif n % a == 12:
                number += "C"
            elif n % a == 13:
                number += "D"
            elif n % a == 14:
                number += "E"
            elif n % a == 15:
                number += "F"
        n //= a
    return number[::-1]


def different_digits(a, b):
    for x in range(len(a)):
        if a[x] in b:
            return False
    return True


def ex20(a, b):
    for x in range(2, 17):
        if different_digits(change_system(a, x), change_system(b, x)):
            return x
    return False
# if appropriate base doesn't exist
# a, b - given numbers from the user
# x - number system base


print(ex20(123, 522))
