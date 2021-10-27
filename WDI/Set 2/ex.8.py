# 8. Some numbers we can't represent as a sum of Fibonacci sequence contiguous elements e.g. 9, 14, 15, 17, 22. Write
# program that for given number (if we can't perform that operation) computes next one for which it is possible.
# Example: for 9 that will be 10, because 2+3+5=10 (Fibonacci sequence elements). If for given number we can simply
# perform that operation program should just return it.

def ex8(n):
    a, b, suma, k, solution = 1, 1, 1, 10**10, 0
    x, y = 1, 1
    while b <= n:
        a, b = b, a+b
        suma += a
        if suma == n:
            return n
        elif suma > n and suma - n < k:
            k = suma - n
            solution = suma
        while suma >= n:
            if suma == n:
                return n
            elif suma - n < k:
                k = suma - n
                solution = suma
            suma -= x
            x, y = y, x + y
    return solution


print(ex8(187))
