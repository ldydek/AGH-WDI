# I start from the end of the number and look for first possible cut (prime number). If this cut was found I recursively
# call a function on the remaining piece and repeat the action. Additionally, I keep variable counting number of made
# cuts. At the end, when we reach 0 (starting number consists of prime number pieces) and quantity of cuts is also
# a prime number function returns true value. If this happens, we finish recursion and true number is returned. When
# this situation won't happen entire recursion returns false value.
# Passed all tests

def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**(1/2))+1):
        if n % x == 0:
            return False
    return True


def divide_rec(n, pieces):
    ctr = 1
    while n:
        if prime(n % ctr):
            if divide_rec(n//ctr, pieces+1):
                return True
        if ctr > n:
            return False
        ctr *= 10
    if prime(pieces):
        return True


def divide(n):
    pieces = 0
    return divide_rec(n, pieces)


print(divide(21722))
