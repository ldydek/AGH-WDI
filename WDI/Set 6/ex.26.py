# 26. We can use A digits 1 and B digits 0, where A,B > 0, to build a number in a binary number system. Write function
# returning quantity of all possible numbers to build for which first digit (the oldest bit) in a binary system number
# is 1 and built number is not prime.
# Solution: using recursion I consider every possible binary sequence (note that we talk about sequences not sets so
# 110 is something different then 101). In a recursive function I keep also additional variables which help me to change
# certain number to decimal number system quite fast and to return final solution.


# function for checking if given number is prime
def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


# main recursive function
def ex26(A, B, decimal, ctr, sol):
    if A == 1 and B == 0:
        decimal += 2**ctr
        if prime(decimal) is False:
            sol[0] += 1
        return sol
    # let's take 1
    if A > 1:
        ex26(A-1, B, decimal+2**ctr, ctr+1, sol)
    # let's take 0
    if B > 0:
        ex26(A, B-1, decimal, ctr+1, sol)


sol = [0]
ex26(2, 3, 0, 0, sol)
print(sol[0])
