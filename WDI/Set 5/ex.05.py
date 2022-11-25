# 05. There is given set o points on a plane described by the structure data = [(x1,y1), (x2,y2), (x3,y3),...(xn,yn)].
# Write a function which returns value True if in a set exist 4 points determining a square with sides parallel to
# coordinate system axes.
# Solution: using four loops we consider every four element in an array. Later thanks to additional function at first
# we check if given four points create an appropriate square. If so then we check if some point different from chose
# as a square corners is inside this square. If that point does not exist we can simply return true value.


# function checking if point is inside a square created by points in "corners" array
def inside(corners, point):
    l, r, b, t = float("inf"), -float("inf"), float("inf"), -float("inf")
    for x, y in corners:
        l = min(l, x)
        r = max(r, x)
        b = min(b, y)
        t = max(t, y)
    return l < point[0] < r and b < point[1] < t


# function checking if four points create a square with sides parallel to the coordinate system axes
def square(points):
    x_arr = []
    y_arr = []
    for x, y in points:
        if x not in x_arr:
            x_arr += [x]
        if y not in y_arr:
            y_arr += [y]
    return len(x_arr) == 2 and len(y_arr) == 2


# main function
def ex05(arr):
    n = len(arr)
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                for d in range(c+1, n):
                    if square((arr[a], arr[b], arr[c], arr[d])):
                        flag = False
                        for e in range(n):
                            if e == a or e == b or e == c or e == d:
                                continue
                            if inside((arr[a], arr[b], arr[c], arr[d]), arr[e]):
                                flag = True
                                break
                        if flag is False:
                            return True
    return False


data = [(0, 2), (0, 2), (2, 0), (2, 2), (-10, 1), (100, 1)]
print(ex05(data))
