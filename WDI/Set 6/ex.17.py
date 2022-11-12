# 17. There are given two integers. We try to create the third one which consists of digits present in both integers.
# What is important is that order of digits in both numbers has to be preserved, for instance, having 123 and 75 we can
# create several numbers. Here are examples: 12375, 17523, 75123, 17253 etc. Write function printing quantity of all
# that prime numbers.
# Solution: inside recursive function we make two calls - one from first number, second one from second number.
# Recursion finishes when these two numbers become 0. Note that final number is created from the end of these two
# integers. At the end, we have to simply check if created number is prime and if so increment a counter.


def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def ex17(n1, n2, ctr=0, number=0):
    ctr1 = 0
    if n1 == 0 and n2 == 0 and prime(number):
        ctr1 += 1
    if n1 > 0:
        ctr1 += ex17(n1//10, n2, ctr+1, number+n1 % 10*10**ctr)
    if n2 > 0:
        ctr1 += ex17(n1, n2//10, ctr+1, number+n2 % 10*10**ctr)
    return ctr1


print(ex17(2373, 77))
