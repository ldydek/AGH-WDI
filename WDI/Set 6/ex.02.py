# 02. We define number "weight" as a quantity of distinct prime number factors e.g. weight(1) = 0, weight(2) = 1,
# weight(30) = 3, weight(64) = 1. We have a given array arr[N] containing natural numbers. Write program checking
# if we can divide array elements for three subsets. Weights sum of given numbers in each subset has to be the same.
# At the end, program should return boolean value.
# Solution: I use auxiliary function to easily change array numbers for their weights. Later, I check if sum of new
# elements is divisible by 3. If not, I can simply return "False", but if so, using recursion to check if this division
# is possible is a good option. So I maintain in an auxiliary array sum of elements in each subset and when all these
# sums are equal it means that this division exists. Note that during recursive returns I subtract certain value to
# add it somewhere else.


def weight(n):
    k, ctr = 2, 0
    while n != 1:
        while n % k == 0:
            n //= k
            ctr += 1
            break
        k += 1
    return ctr
# function computing weight of given number


def ex02(arr):
    n = len(arr)
    arr_sum = [0, 0, 0]
    for x in range(n):
        arr[x] = weight(arr[x])
    # I change array elements for their weights

    suma = 0
    for x in range(n):
        suma += arr[x]
    # checking if sum is divisible by 3 (the same shorter sum(arr))

    if suma % 3:
        return False
    elif ex02_recu(arr, arr_sum, 0):
        return True
    return False


def ex02_recu(arr, arr_sum, x):
    if arr_sum[0] == arr_sum[1] == arr_sum[2] and arr_sum[0] != 0:
        return True
    # "arr_sum[0] != 0" is obligatory, because at the beginning all elements in "arr_sum" are equal to 0
    if x == len(arr):
        return False
    # if array index is out of range recursion is forced to return
    for y in range(3):
        arr_sum[y] += arr[x]
        if ex02_recu(arr, arr_sum, x+1):
            return True
        arr_sum[y] -= arr[x]
    # if computed division is not suitable I am forced to subtract certain element from one subset to add it later to
    # another one


arr = [30, 30, 1, 1, 10, 2]
print(ex02(arr))
