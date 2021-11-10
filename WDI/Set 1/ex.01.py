# 1. Print all Fibonacci sequence elements smaller than million.
# Solution: I use here convenient change of variable values that Python gives us. If variable "a" value will exceed
# 10**6 while loop will be broken.

def zad1():
    a, b = 1, 1
    while a < 10**6:
        print(a, end=" ")
        a, b = b, a + b


zad1()
