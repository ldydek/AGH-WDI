# 08. Same exercise as 07 but this time I can put weights on both scale pans.
# Solution: Analogous problem but this time we have to consider also adding weights to our temporary result not only
# subtracting.


def ex08_recu(arr, k, i):
    if k == 0:
        return True
    if i < 0:
        return False
    return ex08_recu(arr, k, i-1) or ex08_recu(arr, k-arr[i], i-1) or ex08_recu(arr, k+arr[i], i-1)


arr = [1, 2, 5, 4, 7]
print(ex08_recu(arr, 29, len(arr)-1))
