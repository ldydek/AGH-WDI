# 5. Write program in which we enter various numbers and, additionally, we treat 0 only as end of data marker.
# Program should return tenth biggest number from all of them. We can suppose that there is sufficient quantity
# of elements.


def ex5():
    x = int(input())
    arr = []
    while x:
        arr.append(x)
        x = int(input())
    arr.sort()
    return arr[9]


print(ex5())
