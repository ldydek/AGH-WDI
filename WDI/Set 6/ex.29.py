# 29. Point in space is described by three of numbers of a float type (x,y,z). Array T[N] contains N numbers that are
# in space. Points have unitary mass. Write a function which informs us whether there is subset of at least 3 points
# which centroid lies in a distance not bigger than centre of coordinate system.
# Solution: I recursively consider each subset of points. If it has more than 2 points I call additional functions
# which compute distance of this subset of points centroid from centre of coordinate system.


# function computing centroid of certain points
def centroid(arr):
    n = len(arr)
    a, b, c = 0, 0, 0
    for x, y, z in arr:
        a += x
        b += y
        c += z
    return a/n, b/n, c/n


# function computing distance of centroid from (0,0,0)
def distance(a):
    return (a[0]**2 + a[1]**2 + a[2]**2) ** (1/2)


# main recursive function
# (either we include certain point in a solution or simply omit it - so two recursive calls)
def ex29_reku(T, r, points, index):
    if len(points) >= 3 and distance(centroid(points)) <= r:
        return True
    if index == len(T):
        return False
    if ex29_reku(T, r, points+[T[index]], index+1) or ex29_reku(T, r, points, index+1):
        return True
    return False


def ex29(T, r):
    points = []
    return ex29_reku(T, r, points, 0)


T = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
print(ex29(T, 1))
