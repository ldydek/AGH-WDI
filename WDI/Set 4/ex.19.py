# 19. There is a given 2d array with natural numbers. Write program that returns number of elements pairs of a certain
# product. However, there is an additional condition - elements have to lie in a distance of one chess knight's move.
# Solution: I allocate additional array with possible moves by chess knight and later I check if I'd stay on the board
# after jump. If so, I count product of certain two numbers. At the end, we divide ctr by 2, because each solution was
# counted twice (if a*b=k firstly we were on "a" and later on "b").
# arr, k - given array and product
# ctr - number of searched pairs


def ex19(arr, k):
    moves = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    n, ctr = len(arr), 0
    for x in range(n):
        for y in range(n):
            for z in range(len(moves)):
                if 0 <= x + moves[z][0] <= n-1 and 0 <= y + moves[z][1] <= n-1:
                    if k == arr[x][y] * arr[x+moves[z][0]][y+moves[z][1]]:
                        ctr += 1
    ctr //= 2
    return ctr


arr = [[10, 7, 1, 5, 3], [9, 6, 1, 8, 2], [1, 2, 3, 7, 2], [7, 1, 30, 11, 10], [6, 5, 8, 9, 13]]
print(ex19(arr, 20))


