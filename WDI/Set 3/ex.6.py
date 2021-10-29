# 6. Write program checking whether every number in an array contain at least one odd digit.


def odd_digit(a):
    while a > 0:
        if a % 2:
            return True
        a //= 10
    return False


def ex6(arr, n):
    for x in range(n):
        if odd_digit(arr[x]) is False:
            return False
    return True


arr = [1, 212, 345, 32, 246, 90, 56]
n = len(arr)
print(ex6(arr, n))
