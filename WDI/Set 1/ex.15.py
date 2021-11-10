# 15. There is an infinity product: sqrt(0.5) * sqrt(0.5 + 0.5 * sqrt(0.5)) * sqrt(0.5 + 0.5 * 
# sqrt(0.5 + 0.5 * sqrt(0.5))) * ... = 2/pi. Write program that computes pi value using this equation.
# Solution: I repeat multiplying consecutive elements of this product until I gain suitable accuracy. If so, number
# pi has to be approximately equal to 2/product value, where "product" is a product of all elements encountered so far.

from math import pi


def ex15():
    product, e = 1, (1/2)**(1/2)
    while abs(2/pi - product) > 10**(-10):
        product *= e
        e = (1/2 + e/2)**(1/2)
    return 2/product


print(ex15())
