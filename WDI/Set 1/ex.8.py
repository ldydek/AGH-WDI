# 8. Write program that checks if given number is prime.


def ex8(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


print(ex8(97))
