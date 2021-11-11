# 3. We have given 2d array with natural numbers. Write program checking if there is a row in which every number
# contain at least one even digit.

def even_digit(a):
    while a:
        if a % 2 == 0:
            return True
        a //= 10
    return False


def ex2(arr):
    n = len(arr)
    for x in range(n):
        ctr = 0
        for y in range(n):
            if even_digit(arr[x][y]):
                ctr += 1
        if ctr == n:
            return True
    return False


arr = [[390, 2, 5], [4, 55, 10], [57, 90, 100]]
print(ex2(arr))
