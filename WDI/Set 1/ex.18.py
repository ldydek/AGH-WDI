# 18. Modify program from exercise 5. Now it has to compute cube root.
# Solution: Same idea but this time not for a rectangle but for cuboid. For more accurate explanation check exercise 5.

def ex18(n):
    a, b, c, e = 1, 1, n, 10**(-10)
    while abs(c-a) > e:
        a = (a+c)/2
        b = (b+c)/2
        c = n/(a*b)
    return c


print(ex18(125))
