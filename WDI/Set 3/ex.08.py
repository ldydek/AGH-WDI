# 8. There is a given 1d array with natural numbers. We can jump in it from field with index "k" to field with index
# "k+n" if "n" value is a prime factor of T[k], where T is our given array. Write program checking if there is
# a possibility to move from first element to the last one.
# Solution: I allocate auxiliary array which contains only logical values. While considering certain element in a "T"
# array when there is a possibility to move somewhere to the right I change value in the auxiliary array from 0 to 1.
# At the end, I check value of the last element and when it's equal to 1 it means certain sequence of moves exists.


def ex8(arr):
    n = len(arr)
    visited = [False]*n
    visited[0] = True

    for x in range(n):
        if visited[x]:
            divisor = 2
            while arr[x] > 1 and x + divisor <= n-1:
                while arr[x] % divisor == 0:
                    visited[x+divisor] = True
                    arr[x] //= divisor
                divisor += 1
    return visited[n-1]


arr = [2, 5, 4, 1, 9, 7, 2, 3]
print(ex8(arr))
