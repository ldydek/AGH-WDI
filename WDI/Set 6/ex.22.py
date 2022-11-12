# 22. We have given array T[N] with integers. We can jump on that board according to the following rule: from a field
# with index "i" we can jump to field "i+k" if "k" is a prime factor of T[i] lower than T[i]. Write function informs us
# whether we are able to jump from first to last list element. Function should return quantity of jumps or -1 if it's
# not possible.
# Solution: For each element we compute during recursion all its prime factors. During recursion we choose this integers
# and we try to move further in the list. If doing it at some point is not possible we back one level to the top in
# a recursive tree (in other words one recursive back) and check remaining possibilities (backtracking approach).
# At the end, if we find a solution thanks to additional variable we can count number of levels in a recursive tree
# and this will be a solution.

# function for checking if given number is prime
def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


# function computing all prime factors of a certain integer
def prime_factors(n):
    factors = [0 for _ in range(n+1)]
    for x in range(2, int(n**0.5)+1):
        if n % x == 0 and prime(x) is True:
            factors[x] = 1
            if prime(n//x):
                factors[n//x] = 1
    return factors


# recursive function
def ex22(arr, index):
    # if we reach the end we can start counting number of jumps
    if index == len(arr)-1:
        return 0
    factors = prime_factors(arr[index])
    for x in range(2, int(arr[index]**0.5)+1):
        if factors[x] == 1 and x < arr[index] and index + x < len(arr):
            answer = ex22(arr, index+x)
            # answer variable keeps returning values of a recursive calls
            # if it is not negative it means that path was found
            if answer >= 0:
                return answer + 1
        # simultaneously with above condition we can consider this one below, because if "x" is a factor of "n", then
        # "n"//"x" is a factor of "n" as well
        if factors[arr[index]//x] == 1 and arr[index]//x < arr[index] and index + arr[index]//x < len(arr):
            answer = ex22(arr, index+arr[index]//x)
            if answer >= 0:
                return answer + 1
    return -1


arr = [9, 9, 8, 9, 6, 10, 1]
print(ex22(arr, 0))
