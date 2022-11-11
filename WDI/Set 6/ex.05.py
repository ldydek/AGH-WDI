# 5. There is given sequence of 0 and 1 written in T[N]. Write function which answers for a question if it is possible
# to cut given number into pieces and each piece represents a prime number. Length of each piece can't exceed 30.
# Solution: I move from the end of the array and if prime number is found I recursively check remaining part.

# function for checking if given number is prime
def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


# main function for exercise 5 in which there is a recursive function with additional parameter
def ex5(arr):
    n = len(arr)
    if arr[n-1] == 0:
        return False
    return ex5_reku(arr, n-1)


# recursive function - "end" represents last index of considering subarray
def ex5_reku(arr, end):
    # if representing subarray ends with 0 cutting it with prime numbers is not possible
    if arr[end] == 0:
        return False
    # if "ends" become negative it means that we found appropriate cuts
    if end < 0:
        return True
    piece_length = 0
    number = 0
    while piece_length < 30 and end >= 0:
        number += arr[end] * 10 ** piece_length
        piece_length += 1
        end -= 1
        # number can't start with 0 - we move to the next loop stage
        if arr[end+1] == 0:
            continue
        if prime(number):
            # now if recursive function returns True at one point we can easily finish recursion without considering
            # another cases - we have to determine if it is possible to cut given number not find all possible number
            # of cuts
            if ex5_reku(arr, end):
                return True
    return False


arr = [1, 0, 1, 1, 0, 1]
print(ex5(arr))
# True 101|101
