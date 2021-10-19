# 3. Write a program that checks if contiguous subsequence summing up to a certain number exists in a Fibonacci
# sequence.
# Solution: Idea is to iterate from the beginning and when temporary sum exceeds our number, we start
# subtracting elements of the Fibonacci sequence from the beginning (because subsequence has to be contiguous).
def ex3(k):
    suma = 0
    a, b, p, q = 0, 1, 0, 1
    while a <= k:
        if suma == k:
            return True
        suma += a
        a, b = b, a + b
        while suma > k:
            suma -= p
            p, q = q, p + q
    return False


print(ex3(3))
