# 2. Find beginning elements instead of 1, 1 of minimum sum that analogous sequence to Fibonacci sequence will contain
# an element equal to this year number.

def ex2():
    a, b = 2020, 2020
    an, bn = 0, 0
    for x in range(1, a//2):
        for y in range(1, a//2):
            c, d = x, y
            xd, ty = x, y
            while d < a:
                c, d = d, c+d
            if d == a and xd + ty < b:
                b = xd+ty
                an, bn = xd, ty
    return an, bn


print(ex2())
