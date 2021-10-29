# 11. Write program which determines the length of the longest contiguous geometric subsequence in a given array.

def ex11(arr):
    n, solution, ctr = len(arr), 2, 2
    if n == 1:
        return 1
    for x in range(1, n-1):
        k = arr[x]/arr[x-1]
        if arr[x+1]/arr[x] == k:
            ctr += 1
        else:
            solution = max(solution, ctr)
            ctr = 2
    solution = max(solution, ctr)
    return solution


arr = [2, 5, 3/2, 3, 6, 12, 24, 48]
print(ex11(arr))
