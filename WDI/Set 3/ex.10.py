# 10. Write program which determines the length of the longest contiguous arithmetic subsequence in a given array.

def ex10(arr):
    n, solution, ctr = len(arr), 0, 2
    for x in range(1, n-1):
        k = arr[x]-arr[x-1]
        if arr[x+1] - arr[x] == k:
            ctr += 1
        else:
            solution = max(solution, ctr)
            ctr = 2
    solution = max(solution, ctr)
    return solution


arr = [2, 5, 3, 6, 9, 12]
print(ex10(arr))
