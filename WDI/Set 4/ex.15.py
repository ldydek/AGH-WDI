# 15. There is a given 2d array with natural numbers. Write program checking whether in that array exists a row in which
# every number has at least one prime digit.

def prime_digit(a, primes):
    while a:
        if a % 10 in primes:
            return True
        a //= 10
    return False


def ex15(arr):
    primes = [2, 3, 5, 7]
    n = len(arr)
    for x in range(n):
        k = True
        for y in range(n):
            if prime_digit(arr[x][y], primes) is False:
                k = False
                break
        if k:
            return True
    return False


arr = [[111, 3, 5, 7], [12, 120, 83, 6], [5, 4, 3, 5], [11, 2, 7, 3]]
print(ex15(arr))
