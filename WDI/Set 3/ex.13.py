# 13. We have a given array with pseudorandom numbers. Write program which computes the length of the longest contiguous
# subsequence for which we can find also the reverse of it in that array. Note that e.g. for [2, 1, 3, 1, 2] is
# a reverse itself.
# Solution: We move either front pointer (b) if previous subsequence reverse was found, or (a) otherwise.


def ex13(arr):
    n = len(arr)
    a, b, solution = 0, 1, 1
    while b <= n:
        boole = False
        k = arr[a:b]
        k = k[::-1]
        for x in range(n-1, -1, -1):
            if x - (b-a-1) >= 0 and arr[x-(b-a-1):x+1] == k:
                solution = max(solution, b-a)
                boole = True
                break
        if boole:
            b += 1
        else:
            a += 1
    return solution


arr = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
print(ex13(arr))
# answer is 4, because [9, 3, 1, 7] and [7, 1, 3, 9] are in that array and we won't find any longer subsequence
