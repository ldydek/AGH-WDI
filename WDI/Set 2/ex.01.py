# 1. Write program checking if given number from the user is a product of any two Fibonacci sequence elements.
# Solution: At first I compute square root of the number and find two neighbouring elements of that square root that
# are in a Fibonacci sequence. Later if product of this elements is bigger than our number or not I move forwards or
# backwards in this sequence and consider different pair of the elements. If given number is a product program
# additionally prints this sequence elements not only informs it's true.

def ex1(n):
    a, b = 1, 1
    prev, next = 1, 1

    while b < n**(1/2):
        a, b = b, a+b
        prev, next = a, b
    if b ** 2 == n:
        return b, b

    while a >= 1 and b <= n:
        if a*b == n:
            return a, b
        elif a*b > n:
            a, next = next-a, a
        else:
            prev, b = b, b + prev
    return False


n = int(input())
print(ex1(n))
