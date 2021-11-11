# 7. There are given 2 arrays: T1[N][N] and T2[M], where M = N^2. In each row in T1 elements are natural numbers and are
# sorted non decreasingly. Write program rewriting all elements from T1 to T2 and, at the end, elements in T2 should be
# also sorted non decreasingly.


def ex7(T1):
    n = len(T1)
    T2 = [0]*(n**2)
    for x in range(n):
        for y in range(n):
            T2[x*n+y] = T1[x][y]
    T2.sort()
    return T2


T1 = [[1, 1, 8, 9], [1, 4, 7, 8], [3, 5, 5, 10], [3, 7, 11, 13]]
print(ex7(T1))
