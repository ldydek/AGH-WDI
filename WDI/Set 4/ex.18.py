# 18. We have a given 2d array with integers. Write program which will find contiguous subsequence of elements located
# vertically or horizontally with the largest sum. Maximum subsequence length can be equal to 10. Program should
# simply return this maximum sum.
# Solution: for each column and row we call a function computing sum of a certain consistent subsequence elements with
# a biggest possible sum inside each row and column. In this function we use something called prefix sum to determine
# desired sum quite fast.


# function returning maximum sum of all elements in a certain consistent subsequence
def consistent_sequence(arr):
    n = len(arr)
    aux_arr = [0] * n
    for x in range(n):
        aux_arr[x] = arr[x]
    for x in range(1, n):
        aux_arr[x] += aux_arr[x-1]
    value = 0
    for x in range(n):
        for y in range(x, n):
            if y - x + 1 <= 10:
                value = max(value, sum_between_indexes(aux_arr, x, y))
    return value


# function computing sum between two certain indexes in an array including arr[a] and arr[b] as well
def sum_between_indexes(arr, a, b):
    if a == 0:
        return arr[b]
    return arr[b] - arr[a-1]


# function returning column with index "i" from a matrix
def column(matrix, i):
    return [row[i] for row in matrix]


# main function
def ex18(arr):
    n = len(arr)
    solution = 0
    for x in range(n):
        solution = max(solution, consistent_sequence(arr[x]))
    for x in range(n):
        solution = max(solution, consistent_sequence(column(arr, x)))
    return solution


matrix = [[5, 8, 9, 4, 1, 8, 5, 9, 4, 10, 4, 3, 2, 9, 5],
          [2, 7, 9, 4, 9, 4, 9, 6, 9, 9, 3, 8, 4, 8, 10],
          [5, 1, 9, 6, 1, 9, 8, 6, 4, 6, 4, 2, 2, 3, 5],
          [2, 4, 5, 1, 9, 7, 1, 2, 0, 5, 0, 5, 3, 8, 9],
          [2, 3, 8, 3, 1, 2, 9, 6, 7, 1, 7, 4, 7, 2, 7],
          [0, 9, 5, 7, 3, 4, 0, 9, 5, 2, 7, 4, 2, 0, 2],
          [3, 0, 2, 0, 3, 8, 7, 7, 3, 8, 7, 6, 0, 9, 1],
          [5, 6, 3, 9, 5, 9, 9, 0, 1, 2, 5, 8, 7, 2, 3],
          [9, 5, 0, 2, 9, 0, 9, 8, 5, 2, 0, 5, 5, 8, 2],
          [7, 4, 0, 6, 5, 8, 2, 3, 1, 3, 7, 7, 4, 2, 3],
          [7, 4, 7, 2, 5, 5, 6, 0, 7, 5, 6, 9, 1, 2, 2],
          [1, 9, 3, 8, 8, 8, 2, 0, 8, 6, 4, 0, 2, 6, 1],
          [4, 9, 0, 3, 7, 5, 5, 4, 6, 4, 9, 7, 1, 6, 7],
          [5, 4, 2, 6, 4, 6, 9, 8, 4, 7, 1, 6, 4, 0, 5],
          [6, 7, 6, 2, 6, 7, 5, 0, 4, 3, 4, 9, 4, 0, 2]]
print(ex18(matrix))
