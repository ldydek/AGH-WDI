# 15. Write program computing all n-digit numbers, which sum of all digits raised to the nth power equals this number.
# They are called narcissistic number.

def sum(n, k):
    sum = 0
    while n:
        sum += (n % 10)**k
        n //= 10
    return sum


def ex15(n):
    for x in range(10**(n-1), 10**n):
        if sum(x, n) == x:
            print(x, end=" ")


ex15(3)
