# 12. Write program that informs us whether given number contains a digit equal to the number of its digits.

from math import log10


def ex12(n):
    x = int(log10(n))+1
    # thanks to log10 function we can find a number of digits with ease
    while n > 0:
        if n % 10 == x:
            return True
        n //= 10
    return False


print(ex12(123633))
