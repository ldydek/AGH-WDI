# 2. We have given 2d array filled with natural numbers. Write program checking whether in each row there is at least
# one number consisting of only odd digits.


def odd_digits(a):
    while a:
        if a % 2 == 0:
            return False
        a //= 10
    return True


def ex2(arr):
    n = len(arr)
    for x in range(n):
        boole = False
        for y in range(n):
            if odd_digits(arr[x][y]):
                boole = True
                break
        if boole is False:
            return False
    return True


arr = [[39, 2, 5], [4, 55, 10], [56, 90, 100]]
print(ex2(arr))
