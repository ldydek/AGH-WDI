# 21. Array T[8][8] contains integers. Write function checking whether we can choose from that matrix elements that sum
# up to certain number "k". Additional condition says that any of two sum elements can't be in the same row or in the
# same column. To the main function you can only pass an array and a sum "k". Here is presented additional
# implementation with choosing appropriate fields in a board ("solution" and "temp_solution" variables).
# Solution: when I choose a certain integer from a board I change value in "row" and "column" list from 0 to 1. It means
# that later I will not be able to choose a number that is located in the same row or column. When I choose as many
# numbers as I can and don't find a solution I use backtracking and try to choose different number considering previous
# case (example: I choose 8 integers and didn't find a solution, so I back recursively to 7th integer and try to find
# better field for it etc.). Additionally, during recursive backs I change values in "row" and "column" lists again to
# 0, because we didn't include certain number to a solution.


# recursive function
def ex21_reku(arr, row, column, k, temp_solution, solution):
    if k == 0:
        # we found solution so we can eventually modify "solution" list
        solution[0] = temp_solution
        return True
    for x in range(len(arr)):
        for y in range(len(arr)):
            if row[x] == 0 and column[y] == 0:
                row[x] = 1
                column[y] = 1
                # possible part of a solution - arr[x][y], so we change values to 1 in a lists
                if ex21_reku(arr, row, column, k-arr[x][y], temp_solution+[(x,y)], solution):
                    return True
                row[x] = 0
                column[y] = 0
                # unfortunately choosing that integer didn't lead to a solution so we back value to 0 again in a lists


# main function
def ex21(arr, k):
    n = len(arr)
    row = [0] * n
    column = [0] * n
    temp_solution = []
    solution = [None]
    if ex21_reku(arr, row, column, k, temp_solution, solution):
        return solution
    return False


arr = [[10, 12, 15, 3, 5, 6, 10, 11],
       [1, 5, 7, 1, 4, 10, 9, 2],
       [3, 5, 4, 1, 10, 14, 7, 8],
       [1, 3, 10, 2, 7, 4, 5, 3],
       [10, 32, 4, 32, 65, 4, 2, 1],
       [10, 23, 4, 52, 12, 15, 76, 5],
       [1, 12, 43, 2, 10, 32, 2, 2],
       [10, 3, 56, 21, 12, 34, 12, 10]]
print(ex21(arr, 27))
