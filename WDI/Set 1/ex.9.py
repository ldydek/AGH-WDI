# 9. Write program printing all given number divisors.


def ex9(n):
    for x in range(1, int(n**(1/2))):
        if n % x == 0:
            print(x, n//x, end=" ")
    if n**(1/2) == int(n**(1/2)):
        print(int(n**(1/2)))


ex9(1625)
