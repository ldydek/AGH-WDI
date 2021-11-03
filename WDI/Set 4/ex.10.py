# 10. We have a given 2d array with integer numbers. Write program checking if in each row and each column there is
# at least one 0. If so, program should return "True", otherwise "False". I suppose here that we treat 0 as a number
# not a digit.
# Solution: I allocate here auxiliary array to store information about 0 in columns simultaneously. Thanks to this
# I can traverse this matrix only once. Variable "k" informs us whether in a certain row there is at least one 0. If
# this situation won't happen and "k" will remain False we can simply stop program and return False.

def ex10(arr):
    n = len(arr)
    aux_arr = [0]*n
    for x in range(n):
        k = False
        for y in range(n):
            if arr[x][y] == 0:
                k = True
                aux_arr[y] = 1
        if k is False:
            return False
    for x in aux_arr:
        if x == 0:
            return False
    return True


arr = [[1, 0, 2, 0], [0, 10, 5, 1], [9, 8, 0, 7], [7, 8, 0, 10]]
print(ex10(arr))
