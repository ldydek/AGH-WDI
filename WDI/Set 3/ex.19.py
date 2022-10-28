# 19. We have given an array of length "n", which consists of natural numbers. Write program, which computed the length
# of the longest increasing contiguous subsequence in which sum of all elements is equal to sum of its indexes.
# If this subsequence doesn't exist program should return 0.
# Solution: We start from the beginning counting sum of numbers and indexes to two variables. Let's call them sum1
# and sum2. If sum1 > sum2 we move back pointer and update values of the variables.  If sum1 < sum2 we move
# front pointer.


def ex19(arr):
    n = len(arr)
    a, b, sum1, sum2 = 0, 1, arr[0], 0
    solution = 0
    while b < n-1:
        if arr[b] > arr[b-1]:
            sum1, sum2 = 0, 0
        sum1 += arr[b]
        sum2 += b
        while sum1 > sum2:
            sum1 -= arr[a]
            sum2 -= a
            a += 1
            if a > b:
                b = a
        sum1 = max(sum1, 0)
        sum2 = max(sum2, 0)
        while sum1 < sum2 and b < n-1:
            b += 1
            sum1 += arr[b]
            sum2 += b
        if sum1 == sum2 and sum1:
            solution = max(b-a+1, solution)
    while a != b:
        sum1 -= arr[a]
        sum2 -= a
        a += 1
        if sum1 == sum2 and sum1 != 0:
            solution = max(b-a+1, solution)
    return solution


arr = [1, 2, 1, 3, 1, 8, 6]
print(ex19(arr))
