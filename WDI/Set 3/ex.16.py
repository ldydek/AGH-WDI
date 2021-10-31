# 16. We have a given array. Write program checking whether minimum and maximum elements in it are unique.


def ex16(arr):
    n = len(arr)
    a, b, ctr = -10**10, 10**10, 0
    for x in range(n):
        a = max(a, arr[x])
        b = min(b, arr[x])
    #     a - max, b - min
    for x in range(n):
        if arr[x] == a or arr[x] == b:
            ctr += 1
        if ctr > 2:
            return False
    #   if quantity of these numbers in more than 2, it means that there is at least one additional element
    #   which is either minimum or maximum
    return True


arr = [4, 1, 1, 6, 8, -1, 10, 6]
print(ex16(arr))
