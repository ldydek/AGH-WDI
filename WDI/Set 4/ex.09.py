# 9. We have a given 2d array with natural numbers. Write program checking whether we can find in it a square with odd
# number of elements bigger than 1 for which product of four corner elements is equal to "k". If this square doesn't
# exist program should return "False".


def ex9(arr, k):
    n = len(arr)
    for x in range(n):
        for y in range(n):
            ctr = 2
            while x + ctr < n and y + ctr < n:
                p = arr[x][y]*arr[x+ctr][y]*arr[x][y+ctr]*arr[x+ctr][y+ctr]
                if p == k:
                    return x+ctr//2, y+ctr//2
                ctr += 2
    return False


arr = [[5, 1, 10, 3, 1], [1, 7, 1, 7, 8], [3, 2, 1, 9, 8], [4, 6, 4, 10, 7], [5, 7, 3, 1, 5]]
print(ex9(arr, 150))
