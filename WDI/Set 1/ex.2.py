# 2. Find beginning elements instead of 1, 1 of minimum sum that analogous sequence to Fibonacci sequence will contain
# an element equal to this year number.
# Solution: I check every pair of elements from 1 to floor(a/2) without it and for that pair I start creating sequence
# similar to Fibonacci sequence. "a" - year, "b" - our sum that we are looking for, "c", "d", "xd", "ty" - beginning
# values of considered pair of numbers. One pair is moving to check if 2020 year is in this sequence. If so, we then
# use "c" and "b" to check if c+b is smaller than our temporary sum. If so, I assign these starting numbers to my
# solution ("an", "bn") and modify temporary sum. Note that first element of our pair can be smaller than second.

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
