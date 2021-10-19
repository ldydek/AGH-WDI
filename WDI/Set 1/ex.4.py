# 4. Write program which computes integer part of a square root of a given number, using following:
# 1 + 3 + 5 + ... + n = n^2.
# Solution: when our temporary sum will exceed given number, solution is quantity of while loop performances.

def ex4(n):
    ctr, suma, x = -1, 0, 1
    while suma <= n:
        suma += x
        x += 2
        ctr += 1
    return ctr


print(ex4(345))
