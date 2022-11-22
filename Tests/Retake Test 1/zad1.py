# 1. There is given array T[N] with rational numbers in a fraction forms. Fraction is represented as a tuple (a,b),
# where a is numerator and b is a denominator. Write function longest(T) which returns length of the longest consistent
# geometric subsequence in that array. In case of length equal to 2 function should return 0. We can suppose that given
# array consists of at least two elements.

# Examples:
# print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) - returns 4
# print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # returns 3
# print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # returns 6
# print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # returns 0

# Solution: I want to change this problem to a basic one (finding length of the longest consistent geometric subsequence
# in an array with integers). So my idea is simple: traverse given list once and find longest common multiple of all
# denominators. Now I can extend each fraction and leave only numerators. Now I have basic problem of finding
# subsequence length where array contains only integers.
# Passed all tests


# function computing longest common multiple of two numbers
def lcm(a, b):
    x, y = a, b
    while a != 0:
        a, b = b % a, a
    return (x*y)//b


# function which change each fraction to only its numerator after extending
def change(T, value):
    for x in range(len(T)):
        T[x] = T[x][0] * (value//T[x][1])


# function which finds length of the longest consistent geometric subsequence in an array
def geometric_sequence(arr):
    n, solution, ctr = len(arr), 2, 2
    if n == 1:
        return 1
    for x in range(1, n-1):
        if arr[x-1] == 0:
            continue
        k = arr[x]/arr[x-1]
        if arr[x+1]/arr[x] == k:
            ctr += 1
        else:
            solution = max(solution, ctr)
            ctr = 2
    solution = max(solution, ctr)
    return solution


# main function
def longest(T):
    l_c_m = 1
    for x, y in T:
        l_c_m = lcm(l_c_m, y)
    # computing longest common multiple and leaving only numerators
    change(T, l_c_m)
    length = geometric_sequence(T)
    if length == 2:
        return 0
    return length


T = [(3, 18), (-1, 6), (7, 42), (-1, 6), (5, 30), (-1, 6)]
print(longest(T))
