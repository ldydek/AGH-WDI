# 7. Write program checking whether there is a number in an array, which contains only odd digits.

def odd_digits(a):
    while a:
        if a % 2 == 0:
            return False
        a //= 10
    return True


def ex7(arr):
    for x in range(len(arr)):
        if odd_digits(arr[x]):
            return True
    return False


arr = [34, 12, 67, 56, 9999, 1121]
print(ex7(arr))
