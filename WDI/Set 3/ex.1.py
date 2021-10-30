# 1. Write program changing given number to any number system from 2 to 16.
# "n" - given number, "a" - number system

def ex1(n, a):
    arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    number = ""
    while n:
        number += arr[n % a]
        n //= a
    return number[::-1]


print(ex1(1000, 16))
