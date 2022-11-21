# 27. Square is describes as a four (x_1, x_2, y_1, y_2), where x_1, x_2, y_1, y_2 mean lines and x_1 < x_2 and
# y_1 < y_2. There is given array T with N squares. Write a function which informs us whether in this array we can find
# 13 non-overlapping squares, which surface areas sum is 2012.
# Solution:


def overlap(a, b):
    if a[1] < b[0] or b[1] < a[0] or a[3] < b[2] or b[3] < a[2]:
        return False
    return True


def surface(a):
    return (a[1]-a[0])*(a[3]-a[2])


def overlapping_squares(squares):
    surface_area = 0
    n = len(squares)
    for x in range(n):
        surface_area += surface(squares[x])
        for y in range(x+1, n):
            if overlap(squares[x], squares[y]) is True:
                return
    return surface_area


def ex27(T, index=0, squares=[]):
    if len(squares) > 13 or index == len(T):
        return False
    answer = overlapping_squares(squares)
    if answer is None or answer > 2012:
        return False
    if answer == 2012 and len(squares) == 13:
        return True
    if ex27(T, index+1, squares+[T[index]]) or ex27(T, index+1, squares):
        return True
    return False


T = [(0, 1, 0, 1), (2, 3, 2, 3), (4, 5, 4, 5), (6, 7, 6, 7),
     (8, 9, 8, 9), (10, 11, 10, 11), (12, 13, 12, 13), (14, 15, 14, 15),
     (16, 17, 16, 17), (18, 19, 18, 19), (20, 21, 20, 21), (22, 23, 22, 23),
     (24, 2024, 24, 25), (48, 85, 18, 88)]
print(ex27(T))
