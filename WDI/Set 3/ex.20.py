# 20. There is given array consisting of "n" elements smaller than 1000. Write function computing length of the longest
# consistent subsequence for which product of all its elements every prime factor occurs at most once.
# Solution: I traverse given array and keep two pointers in it. One is at the beginning of considering subsequence, the
# second one at the end. If product doesn't satisfy exercise conditions I move first pointer (the previous one) one
# element further, second pointer jumps next to its friend and repeat the action.


def prime_factor(n):
    for x in range(2, int(n**(1/2))+1):
        if n % (x**2) == 0:
            return False
        if n % x == 0:
            n // x
    return True


def ex20(arr):
    n = len(arr)
    a, solution = 0, 0
    for a in range(n):
        b = a + 1
        product = arr[a]
        while b < n and prime_factor(product):
            product *= arr[b]
            b += 1
        solution = max(solution, b-a-1)
        if prime_factor(product):
            solution = max(solution, b-a)
    return solution


arr = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 17, 257, 277]
# arr = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
print(ex20(arr))
