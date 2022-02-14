# 07. We have a given set of weights written in a 1d array e.g. T = [2, 3, 1] means that first weight has 2kg, second
# 3kg and third 1kg. Write program checking whether using given weights we are able to obtain certain weight.
# Solution: We have two possibilities. Either we include given weight in a solution or not. If certain copy of our
# function returns "True" it means that it's possible and we can simply finish recursion and return "True", but if
# this situation won't happen we can't receive given weight.


def ex07_recu(arr, k, i):
    if k == 0:
        return True
    if i < 0:
        return False
    return ex07_recu(arr, k, i-1) or ex07_recu(arr, k-arr[i], i-1)


arr = [1, 2, 5, 4, 7]
print(ex07_recu(arr, 11, len(arr)-1))
