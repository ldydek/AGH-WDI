# 13. Write program printing the least common multiple (LCM) of three given numbers.
# Solution: LCM(x, y) = x*y / GCD(x, y) (greatest common divisor)


def product_by_gcd(a, b):
    x, y = a, b
    while a != 0:
        a, b = b % a, a
    return (x*y)//b


def ex13(a, b, c):
    return product_by_gcd(product_by_gcd(a, b), c)


print(ex13(101, 201, 4))
