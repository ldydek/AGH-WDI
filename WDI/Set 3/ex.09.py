# 9. Write program which determines the length of the longest contiguous increasing subsequence in a given array.

def ex9(arr):
    n, solution, ctr = len(arr), 0, 1
    for x in range(n-1):
        if arr[x] < arr[x+1]:
            ctr += 1
        else:
            solution = max(solution, ctr)
            ctr = 1
    solution = max(solution, ctr)
    return solution


arr = [1, 1, 2, 3, 2, 1, 10]
print(ex9(arr))
