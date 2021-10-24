# 5. Write program computing square root of a given number using Newton's formula.


def ex5(n):
    a, b, e = 1, n, 10**(-5)
    while abs(b-a) > e:
        a = (a+b)/2
        b = n/a
    return a


print(ex5(25))
