# 8. We have a given 2d array with natural numbers. Write program checking whether in that array exists contiguous
# geometric subsequence located diagonally in direction right-bottom with at least 3 elements. Function should return
# information if that subsequence exists and if so its length as well.


def ex8(arr):
    n = len(arr)
    a, solution = n-3, 0
    while a >= 0:
        ctr1, ctr2, b = 2, 2, 0
        for x in range(a+1, n-1):
            k1 = arr[x][b+1]/arr[x-1][b]
            k2 = arr[b+1][x]/arr[b][x-1]
            if arr[x+1][b+2]/arr[x][b+1] == k1:
                ctr1 += 1
            else:
                solution = max(solution, ctr1)
                ctr1 = 2
            if arr[b+2][x+1]/arr[b+1][x] == k2:
                ctr2 += 1
            else:
                solution = max(solution, ctr2)
                ctr2 = 2
            b += 1
        solution = max(solution, ctr1, ctr2)
        a -= 1
    return solution


arr = [[1, 1, 10, 3, 1], [1, 2, 1, 7, 8], [3, 2, 4, 9, 8], [4, 6, 4, 8, 7], [5, 7, 3, 8, 16]]
print(ex8(arr))
