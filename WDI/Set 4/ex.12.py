# 12. There is a given array T[N][N][N] with positive numbers. Write program returning "True" value if on all levels of
# an array number of elements neighbouring with at least 6 composite numbers is equal or "False" value otherwise.
# We consider all neighbouring elements at the same level.


def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def ex12(arr):
    n, check = len(arr), 0
    moves = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    for a in range(n):
        ctr1 = 0
        for b in range(n):
            for c in range(n):
                ctr = 0
                for d in moves:
                    if 0 <= d[0] + b <= n-1 and 0 <= d[1] + c <= n-1:
                        if prime(arr[a][b+d[0]][c+d[1]]) is False:
                            ctr += 1
                if ctr >= 6:
                    ctr1 += 1
        if a >= 1:
            if ctr1 != check:
                return False
        check = ctr1
    return True


arr = [[[70, 12, 14], [19, 2, 11], [6, 9, 27]], [[21, 8, 10], [30, 3, 27], [15, 18, 16]], [[2, 12, 14], [7, 10, 15],
                                                                                          [25, 21, 18]]]
print(ex12(arr))
