# 4. Two-three-five number in a factorization doesn't have any other prime numbers than 2, 3 and 5. Write program that
# computes how many these numbers is in range from 1 do "n" without "n". We include number 1 as well
# (it's an exception).
# Solution: I check factorization of each number in range from 1 to "n" and if we start dividing certain element by
# a number bigger than 5 it means that this number has to have a prime divisor bigger than 5, because we still didn't
# get 1 (after factorization our beginning number has to be equal to 1) and our temporary number is not already
# divisible by 2, 3 or 5. We assign to "a" value of "x", because later "x" will be modified.

def ex4(n):
    ctr = 0
    for x in range(1, n):
        a, p = x, 1
        while p <= x and p < 5:
            p += 1
            while x % p == 0:
                x //= p
        if x == 1:
            ctr += 1
            print(a, end=" ")
    return ctr


print(ex4(35))
