# 17. There is a 2d array with natural numbers. Write program returning number of row and column of a certain element
# for which sum of surrounding elements is the biggest.
# Solution: To help me check surrounding cells I allocate additional array called "moves". During traversing it
# condition in the internal loop prevent from escaping outside of the board. "solution" keeps the highest sum found
# so far and (a, b) keeps suitable indexes of temporary sum.


def ex17(arr):
    n = len(arr)
    a, b = None, None
    solution = 0
    moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for x in range(n):
        for y in range(n):
            ctr = 0
            for z in range(len(moves)):
                if 0 <= x + moves[z][0] <= n-1 and 0 <= y + moves[z][1] <= n-1:
                    ctr += arr[x+moves[z][0]][y+moves[z][1]]
            if solution < ctr:
                solution = ctr
                a, b = x, y
    return a, b


arr = [[10, 30, 2, 1], [80, 50, 8, 6], [1, 1, 2, 3], [7, 6, 5, 6]]
print(ex17(arr))
# answer here is (0, 0) with sum equal to 160
