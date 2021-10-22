from math import pi


def ex15():
    product, e, eps = 1, (1/2)**(1/2), 10**(-10)
    while abs(2/pi - product) > eps:
        product *= e
        e = (1/2 + e/2)**(1/2)
    return 2/product


print(ex15())
