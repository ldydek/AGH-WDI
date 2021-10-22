# 15. There is an infinity product: sqrt(0.5) * sqrt(0.5 + 0.5 * sqrt(0.5)) * sqrt(0.5 + 0.5 * 
# sqrt(0.5 + 0.5 * sqrt(0.5))) * ... = 2/pi. Write program that computes pi value using this equation.

from math import pi


def ex15():
    product, e, eps = 1, (1/2)**(1/2), 10**(-10)
    while abs(2/pi - product) > eps:
        product *= e
        e = (1/2 + e/2)**(1/2)
    return 2/product


print(ex15())
