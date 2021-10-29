# 8. Write program that checks if given number is prime.
# Solution: If one of elements in range from 2 to floor of square root plus one is divided by this number it means that
# it has a divisor distinct from 1 and this number. If this situation won't happen it means that this number doesn't
# have any divisors bigger than 1 and smaller than this number, so it's prime.

def ex8(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


print(ex8(97))
