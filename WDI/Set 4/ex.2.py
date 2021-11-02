# 2. We have given 2d array filled with natural numbers. Write program checking whether in each row there is at least
# one composite number consisting of only odd digits.


def odd_digits(a):
    while a:
        if a % 2 == 0:
            return False
        a //= 10
    return True


def sieve(arr, n):
    p = 2
    while p * p <= n:
        for x in range(2*p, n, p):
            arr[x] = 0
        p += 1
    return arr


def ex2(arr):
    n = len(arr)
    k = max(arr)
    k = max(k)
    # fast determining the biggest number in a matrix
    aux_arr = [1]*(k+1)
    sieve(aux_arr, k+1)

    for x in range(n):
        boole = False
        for y in range(n):
            if odd_digits(arr[x][y]) and aux_arr[arr[x][y]] == 0:
                boole = True
                break
        if boole is False:
            return False
    return True


arr = [[39, 2, 5], [4, 55, 10], [55, 90, 100]]
print(ex2(arr))
