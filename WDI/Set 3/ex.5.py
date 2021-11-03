# 5. Write program in which we enter various numbers and, additionally, we treat 0 only as end of data marker.
# Program should return tenth biggest number from all of them. We can suppose that there is sufficient quantity
# of elements.
# Solution: We are constantly adding new elements to our growing array and, at the end, we sort all data structure
# and read tenth biggest number.


def ex5():
    x = int(input())
    arr = []
    while x:
        arr.append(x)
        x = int(input())
    arr.sort()
    return arr[9]


print(ex5())
