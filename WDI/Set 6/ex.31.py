# 31. Write a function which gets as a parameter an integer and returns sum of all non-empties sets elements products.
# Sets are created from from all integer prime divisors. For instance, 60 -> [2,3,5] ->
# -> 2 + 3 + 5 + 2*3 + 2*5 + 3*5 + 2*3*5 = 71. We can suppose that quantity of these divisors is not bigger than 20.
# Solution: at the beginning, we use an additional function which computes all integer prime divisors. If we have a list
# of them we can use recursion to get desired value.


def prime_divisors(n):
    # firstly we can allocate array of length 20
    arr = [0] * 20
    index = 0
    d = 2
    while n > 1:
        flag = True
        while n % d == 0:
            if flag:
                arr[index] = d
                index += 1
                flag = False
            n //= d
        d += 1
    # now thanks to "index" variable we can rewrite to the new array all computed divisors and don't bother about
    # the rest of the previous array filled with 0
    aux_arr = [0] * index
    for x in range(index):
        aux_arr[x] = arr[x]
    return aux_arr


def ex31_reku(arr, value=1, index=0):
    sum = 0
    if index == len(arr):
        return value
    sum += ex31_reku(arr, value*arr[index], index+1) + ex31_reku(arr, value, index+1)
    return sum


def ex31(n):
    arr = prime_divisors(n)
    return ex31_reku(arr) - 1
    # note that here we have to subtract 1 because in a recursive function we return value variable which is
    # equal to 1 at the beginning, so for empty set it will return 1, but sets have to be non-empty and we have to
    # exclude that possibility.


print(ex31(60))
