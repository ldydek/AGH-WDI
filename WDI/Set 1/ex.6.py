# 6. Write program solving equation x^x = 2020 by bisection method.
# At first we initialize variables for 0 and for 5, because 5^5 = 3125 and is bigger than 2020. Later if
# ((0+5)/2)**((0+5)/2) is bigger than 2020 or not we change variable "a" or "b" and repeat the same until we achieve
# given accuracy or find suitable number.

def ex6():
    a, b, accuracy = 0, 5, 0.0001
    while b-a > accuracy:
        x = (a+b)/2
        if x**x == 2020:
            return x
        elif x**x > 2020:
            b = x
        else:
            a = x
    return (a+b)/2


print(ex6())

