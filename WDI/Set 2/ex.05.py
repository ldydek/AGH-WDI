# 05. We have given integer with non-repeating digits without digit 0. How many different number divisible by 7 we can
# obtain by crossing out any number of digits in this integer. For instance, for 2315 it will be 21, 35, 231 and 315.
# Solution: using bit mask we can solve this task. Each time we pass a new value from range from 1 to 2^k, where "k" is
# a number length we look for its binary representation. Places where is digit 1 mean that these digits weren't cross
# out. In this tricky way we can consider every possibility of crossing out various digit from an integer.

# function computing number of integer digits
def digits(x):
    ctr = 0
    while x:
        ctr += 1
        x //= 10
    return ctr


def bit_mask(number, mask):
    actual_number = 0
    while number:
        if mask % 2 == 1:
            actual_number *= 10
            actual_number += number % 10
        number //= 10
        mask //= 2
    new_number = 0
    while actual_number:
        new_number *= 10
        new_number += actual_number % 10
        actual_number //= 10
    return new_number


def ex05(n):
    length = digits(n)
    ctr = 0
    for x in range(1, 2**length):
        if bit_mask(n, x) % 7 == 0:
            ctr += 1
    return ctr


print(ex05(77))
