# 6. Write program that represents given number as a product of two elements of the smallest difference. For instance
# 120 = 10*12 and 30=5*6 (not e.g. 30=3*10).

def ex6(n):
    x = int(n**(1/2))
    while n % x:
        x -= 1
    return x, n//x


print(ex6(25))
