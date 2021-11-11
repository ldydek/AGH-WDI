# 6. Write program checking whether every number in an array contain at least one odd digit.
# Solution: odd_digit function checks every digit of a given number and in the main function we call it for each number.


def odd_digit(a):
    while a:
        if a % 2:
            return True
        a //= 10
    return False


def ex6(arr):
    for x in range(len(arr)):
        if odd_digit(arr[x]) is False:
            return False
    return True


arr = [1, 212, 345, 32, 246, 90, 56]
print(ex6(arr))
