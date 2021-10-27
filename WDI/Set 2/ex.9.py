# 9. Write program that computes surface area under the figure f(x) = 1/x from 1 to "k" by rectangles method.
# We assume that k > 1.

def f(x):
    return 1/x


def ex9(k):
    e, x = 10**(-5), 1
    surface = 0
    while x < k:
        surface += e*(f(x)+f(x+e))/2
        x += e
    return surface


print(ex9(5))
