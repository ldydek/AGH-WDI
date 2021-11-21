# 01. Write program which prints for a given integer all prime numbers which consist of at least two digits and we can
# create them by deleting at least one digit from the original integer.
# Solution: I build a recursive tree. At each level of it I delete one digit and recursively call a function for the
# remaining pieces. To print a number only once found integers so far I keep in an auxiliary array with solutions.
# "l" variable helps me consider only these integers with at least one deleted digit.


def length(n):
    ctr = 0
    while n:
        ctr += 1
        n //= 10
    return ctr


def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def ex1(n):
    def ex1_recu(n, k, solution):
        for x in range(k):
            ex1_recu(n//(10**(x+1)) * 10 ** x + (n % (10**x)), k-1, solution)
            l = n//(10**(x+1)) * 10 ** x + (n % (10**x))
            if prime(l) and l // 10 != 0 and l not in solution:
                solution.append(l)
    k = length(n)
    solution = []
    ex1_recu(n, k, solution)
    return solution


print(ex1(2573))
