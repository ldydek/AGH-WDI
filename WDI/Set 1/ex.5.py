# 5. Write program computing square root of a given number using Newton's formula.
# Solution: We can think about it in this way: at first we have a rectangle 1xn, where "n" is
# our given number. Our goal is to change length of rectangle sides to obtain a square, but
# its surface has to be the same all the time.


def ex5(n):
    a, b, e = 1, n, 10**(-5)
    while abs(b-a) > e:
        a = (a+b)/2
        b = n/a
    return a


print(ex5(25))
