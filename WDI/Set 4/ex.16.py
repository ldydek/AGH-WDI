# 16. We have 2d array with natural numbers. Write program checking whether each row in the array contain at least
# one composite number in which all digits are prime numbers.


def prime_digits(a, primes):
    while a:
        if a % 10 not in primes:
            return False
        a //= 10
    return True


def prime_number(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def ex16(arr):
    n = len(arr)
    primes = [2, 3, 5, 7]
    for x in range(n):
        k = False
        for y in range(n):
            if prime_number(arr[x][y]) is False and prime_digits(arr[x][y], primes):
                k = True
                break
        if k is False:
            return False
    return True


arr = [[1, 3, 5, 72], [22, 10, 8, 6], [25, 4, 3, 5], [10, 2, 1, 32]]
print(ex16(arr))
