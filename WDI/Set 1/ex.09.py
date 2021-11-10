# 9. Write program printing all given number divisors.
# Solution: We iterate in range from 1 to floor of square root plus one and when we meet a number divisible by "n",
# when "n" is our given number we can print this divisor, let's say "x", and n/x at once.


def ex9(n):
    for x in range(1, int(n**(1/2))):
        if n % x == 0:
            print(x, n//x, end=" ")
    if n**(1/2) == int(n**(1/2)):
        print(int(n**(1/2)))


ex9(1625)
