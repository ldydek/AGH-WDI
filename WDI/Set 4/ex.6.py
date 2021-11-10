# 6. There are given 2 arrays: T1[N][N] and T2[M], where M = N^2. In each row in T1 elements are sorted increasingly.
# Write program rewriting all unique elements from T1 to T2 and, at the end, T2 array also should be sorted
# increasingly.


def ex6(arr):
    n = len(arr)
    arr1 = [0]*(n**2)
    for x in range(n):
        for y in range(n):
            arr1[x*n+y] = arr[x][y]
    arr1.sort()

    for x in range(n**2-1):
        if arr1[x] == arr1[x+1]:
            arr1[x] = 0
    arr1.sort()
    return arr1


arr = [[1, 5, 8, 9], [1, 4, 7, 8], [3, 4, 5, 10], [3, 7, 11, 13]]
print(ex6(arr))
