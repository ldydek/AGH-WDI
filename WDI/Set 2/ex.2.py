# 2. There are given 3 numbers: a, b, n. Write program which prints decimal expansion of fraction a/b that has
# "n" digits after a point.

def ex2(a, b, n):
    ctr = 0
    print(a//b, end=".")
    while ctr < n:
        a = (a % b)*10
        print(a//b, end="")
        ctr += 1


ex2(12, 7, 20)


