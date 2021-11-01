# 12. In a given array there are pseudorandom odd numbers from the range 1-99. Write program that computes a difference
# between lengths of the longest increasing and longest decreasing contiguous arithmetic subsequences.


def ex12(arr):
    n, i, d = len(arr), 0, 0
    if n == 1:
        return 0
    solutioni, solutiond = 0, 0
    for x in range(1, n-1):
        k = arr[x] - arr[x-1]
        if k > 0:
            if arr[x+1] - arr[x] == k:
                i += 1
            else:
                solutioni = max(solutioni, i+1)
                i, d = 1, 1
        else:
            if arr[x+1] - arr[x] == k:
                d += 1
            else:
                solutiond = max(solutiond, d+1)
                i, d = 1, 1
    solutioni = max(solutioni, i)
    solutiond = max(solutiond, d)
    if solutioni == 0:
        return max(solutiond, d+2)
    elif solutiond == 0:
        return max(solutioni, i+2)
    else:
        solutioni += 1
        solutiond += 1
    return abs(solutioni - solutiond)


arr = [-2, -1, 0, 1, -1, -3, -5, -7]
print(ex12(arr))
