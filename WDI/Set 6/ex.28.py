# 28. We have given array T[N] with integers. Write a function which informs us whether there is a possibility to divide
# given set of integers into three subsets. In each subset all quantity of digit 1 which we are using to build these
# numbers in a binary number system should be the same. For instance, [2,3,5,7,15] -> true, because subsets:
# {2,7}, {3,5}, {15} are built with 4 digits 1; [5,7,15] -> false (division does not exist).
# Solution: At the beginning, I change array elements. Each integer will be changed to its quantity of digit 1 in a
# binary number system. Now using recursion we can simply check whether we can divide this array into three subsets
# where elements sum in each subset is the same.

# function returning number of digit 1 in a binary number system
def binary(a):
    ctr = 0
    while a:
        if a % 2 == 1:
            ctr += 1
        a //= 2
    return ctr


# changing array integers here
def change(arr):
    for x in range(len(arr)):
        arr[x] = binary(arr[x])


# main recursive function
def ex28_reku(arr, ctr1, ctr2, ctr3, index):
    if index == len(arr):
        if ctr1 == ctr2 == ctr3:
            return True
        return False
    if ex28_reku(arr, ctr1+arr[index], ctr2, ctr3, index+1):
        return True
    if ex28_reku(arr, ctr1, ctr2+arr[index], ctr3, index+1):
        return True
    if ex28_reku(arr, ctr1, ctr2, ctr3+arr[index], index+1):
        return True
    return False


def ex28(arr):
    change(arr)
    # if sum of all elements is not divisible by 3 it means that an appropriate division does not exist
    if sum(arr) % 3 != 0:
        return False
    ctr1, ctr2, ctr3 = 0, 0, 0
    return ex28_reku(arr, ctr1, ctr2, ctr3, 0)


arr = [2, 3, 5, 7, 15]
print(ex28(arr))

