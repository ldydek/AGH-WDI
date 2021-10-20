# 1. Print all Fibonacci sequence elements smaller than million.

def zad1():
    a, b = 1, 1
    while a < 10**6:
        print(a, end=" ")
        a, b = b, a + b


zad1()
