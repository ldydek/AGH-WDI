# 24. Array T = [(x_1, y_1), (x_2, y_2), (x_3, y_3), ...] contains coordinates of "n" points described in float type.
# Write function computing the lowest possible distance between centroids of two nonempty subsets.
# Solution: we recursively consider every possible situation of elements in two subsets. When recursive function
# generates one of them we call additional function computing centroid of each subset and finally distance between them.
# At the end, I compare given value with computed shortest distance so far.


def centroid(array):
    n = len(array)
    ctr1, ctr2 = 0, 0
    for x, y in array:
        ctr1 += x
        ctr2 += y
    return ctr1/n, ctr2/n


def two_subsets_centroid_distances(x, y):
    return ((x[0]-y[0])**2 + (x[1]-y[1]) ** 2) ** (1/2)


def ex24(arr, solution, subset1=[], subset2=[], index=0):
    if len(subset1) > 0 and len(subset2) > 0:
        solution[0] = min(solution[0], two_subsets_centroid_distances(centroid(subset1), centroid(subset2)))
        return
    if index == len(arr):
        return
    ex24(arr, solution, subset1+[arr[index]], subset2, index+1)
    # adding to the first set
    ex24(arr, solution, subset1, subset2+[arr[index]], index+1)
    # adding to the second set
    ex24(arr, solution, subset1, subset2, index+1)
    # omitting this point


T = [(47, 29), (74, 56), (69, 32), (67, 85), (72, 42), (6, 62), (80, 64), (13, 1), (5, 69), (98, 42)]
solution = [float("inf")]
ex24(T, solution)
print(solution[0])
