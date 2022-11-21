# 32. There is given array T[N] with integers. Write a function which informs us whether we can create two subsets of
# array elements (not necessarily all of them) that have equal elements sum and quantity of elements from both subsets
# is equal to "k". To the function you should pass only array "T" and integer "k". Function should return bool value.
# Solution: simple recursion. I start considering elements from the beginning and have three options. Include it in
# a first set (sum1 value grows), in a second set (sum2 value grows) or simply omit it. When we include somewhere
# certain element, we decrement "k" variable. When it will be 0 it means that we have "k" elements included and if
# additionally sum of all elements in both subsets is the same we can return true value.


def ex32_reku(T, sum1, sum2, k, index=0):
    if k == 0 and sum1 == sum2:
        return True
    if index == len(T):
        return False
    return ex32_reku(T, sum1+T[index], sum2, k-1, index+1) or \
        ex32_reku(T, sum1, sum2+T[index], k-1, index+1) or \
        ex32_reku(T, sum1, sum2, k, index+1)


def ex32(T, k):
    sum1, sum2 = 0, 0
    return ex32_reku(T, sum1, sum2, k)


T = [3, 6, 5, 23, 14, 23, 1, 19, 2, 7, 8, 15]
print(ex32(T, 11))
