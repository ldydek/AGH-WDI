# 10. Computing recursively matrix determinant (obvious content).
# Solution: using recursive Laplace expansion we can easily count determinant of nth degree matrix.

# function for generating new matrix which is built with previous matrix without row "i" and column "j"
def submatrix(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]


# determinant of matrix 2x2
def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# main recursive function
def ex10(matrix):
    n, det = len(matrix), 0
    for x in range(n):
        # base case - matrix 2x2
        if n == 2:
            return determinant(matrix)
        det += matrix[0][x] * (-1) ** (1 + 1+x) * ex10(submatrix(matrix, 0, x))
    return det


matrix = [[0, 1, 2, 7],
          [1, 2, 3, 4],
          [5, 6, 7, 10],
          [-1, 1, -1, -1]]
print(ex10(matrix))
