# 7. Write program that checks if given number is a product of two neighbouring elements in a Fibonacci sequence.
# Solution: We iterate through this sequence and when product of two contiguous elements exceeds given number it means
# that we can't reach this number, but when it's equal it means this number is available.


def ex7(n):
    a, b = 1, 1
    while a*b < n:
        a, b = b, a+b
    if a*b == n:
        return True
    return False


print(ex7(40))
