# 13. Write program printing the least common multiple (LCM) of three given numbers.
# Solution: LCM(x, y) = x*y / GCD(x, y) (greatest common divisor). Note that computing LCM of three numbers as max
# of LCM(x, y), LCM(x, z) and LCM(y, z) is incorrect, because e.g. for 101, 201 and 4 max(LCM(101, 201), LCM(201, 4),
# LCM(101, 4)) is 20301. We have to do it in this way: LCM(x, y, z) = LCM(LCM(x, y), z), so it's 81204.


def lcm(a, b):
    x, y = a, b
    while a != 0:
        a, b = b % a, a
    return (x*y)//b


def ex13(a, b, c):
    return lcm(lcm(a, b), c)


print(ex13(101, 201, 4))
