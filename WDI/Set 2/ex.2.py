# 2. There are given 3 numbers: a, b, n. Write program which prints decimal expansion of fraction a/b that has
# "n" digits after a point.

def ex2(a, b, n):
    print(a//b, end=".")
    while n > 0:
        a = (a % b)*10
        print(a//b, end="")
        n -= 1


ex2(124, 13, 20)


