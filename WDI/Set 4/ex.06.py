# 6. There are given 2 arrays: T1[N][N] and T2[M], where M = N^2. In each row in T1 elements are sorted increasingly.
# Write program rewriting all unique elements from T1 to T2 and, at the end, T2 array also should be sorted
# increasingly.


def ex6(T1):
    n = len(T1)
    T2 = [0]*(n**2)
    for x in range(n):
        for y in range(n):
            T2[x*n+y] = T1[x][y]
    T2.sort()

    for x in range(n**2-1):
        if T2[x] == T2[x+1]:
            T2[x] = 0
    T2.sort()
    return T2


T1 = [[1, 5, 8, 9], [1, 4, 7, 8], [3, 4, 5, 10], [3, 7, 11, 13]]
print(ex6(T1))


arr = [[1, 5, 8, 9], [1, 4, 7, 8], [3, 4, 5, 10], [3, 7, 11, 13]]
print(ex6(arr))
