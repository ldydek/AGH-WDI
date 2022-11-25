# 17. There are given two arrays t1 and t2 of length "n" with natural numbers. We can create sum taking elements from
# both arrays. We call a sum "correct" if it contains at least one element (from t1 or t2 array) with each index.
# For instance, for arrays t1 = [1,3,2,4] and t2 = [9,7,4,8] correct sums are for instance 1+3+2+4, 9+7+4+8+4.
# Write a function generating all correct sums that are prime numbers. To the function you should pass two arrays.
# Function should return quantity of found correct sums.
# Solution: in the solution we use additional array with 0,1,2 values. Number 0 will inform us that we take element from
# first array, number 1 from second one and number 2 from both arrays.


# function writing 0,1,2 values to the auxiliary array
def ternary(array, value):
    n = len(array)
    for x in range(n-1, -1, -1):
        array[x] = value % 3
        value //= 3


# function checking if given number is prime
def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


# function creating new sum according to the auxiliary array values
def create_sum(array, t1, t2):
    n = len(array)
    value = 0
    for x in range(n):
        if array[x] == 0:
            value += t1[x]
        elif array[x] == 1:
            value += t2[x]
        else:
            value += t1[x] + t2[x]
    return value


# main function
def ex17(t1, t2):
    n = len(t1)
    aux_array = [0] * n
    solution = 0
    for x in range(3**n):
        ternary(aux_array, x)
        value = create_sum(aux_array, t1, t2)
        if prime(value):
            solution += 1
    return solution


t1 = [1, 3, 2, 4]
t2 = [9, 7, 4, 8]
print(ex17(t1, t2))
