# 3. Write program computing all prime numbers smaller than "n" by sieve of Eratosthenes algorithm.
# Solution: Idea is to change all array indexes which are multiple of "p" and "p" starts from the
# smallest prime number.

def ex3(n):
    arr = [1]*n
    p = 2
    while p * p <= n:
        for x in range(2*p, n, p):
            arr[x] = 0
        p += 1
    for x in range(2, n):
        if arr[x]:
            print(x, end=" ")


ex3(278)
