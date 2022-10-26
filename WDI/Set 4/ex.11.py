# 11. We call two numbers a "friends" if they are built with the same digits e.g. 123, 321 or 35, 53553. We have a given
# 2d array with natural numbers. Write program computing how many numbers in it are surrounded only by friendly numbers.


def same_digits(a, b, arr):
    while a > 0:
        arr[a % 10] = 1
        a //= 10
    while b > 0:
        if arr[b % 10]:
            arr[b % 10] = 2
        else:
            return False
        b //= 10
    for x in range(10):
        if arr[x] == 1:
            return False
    return True


def ex11(arr):
    n, ctr = len(arr), 0
    for x in range(1, n-1):
        for y in range(1, n-1):
            aux_arr = [0] * 10
            k = True
            for z in range(x-1, x+2):
                if same_digits(arr[z][y-1], arr[x][y], aux_arr) is False or same_digits(arr[z][y+1], arr[x][y], aux_arr) is False:
                    k = False
            if same_digits(arr[x+1][y], arr[x][y], aux_arr) is False or same_digits(arr[x-1][y], arr[x][y], aux_arr) is False:
                k = False
            if k:
                ctr += 1

    return ctr


arr = [[121, 22, 12, 77], [112, 21, 11, 22], [121, 211, 221, 11], [15, 55, 22, 12]]
print(ex11(arr))
