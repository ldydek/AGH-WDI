# 19. Write a program loading two integers "a" and "b", computing decimal expansion of a/b and printing it in a
# repeating decimal form.


def two_five(x):
    ctr2, ctr5 = 0, 0
    while x % 2 == 0:
        ctr2 += 1
        x //= 2
    while x % 5 == 0:
        ctr5 += 1
        x //= 5
    return max(ctr2, ctr5)


def ex19():
    a = int(input("> "))
    b = int(input("> "))
    print(a//b, end="")
    r = a % b
    if r > 0:
        print(".", end="")
        for x in range(two_five(b)):
            r *= 10
            print(r//b, end="")
            r %= b
        if r > 0:
            print("(", end="")
            mem = r
            while True:
                r *= 10
                print(r//b, end="")
                r %= b
                if r == mem:
                    break
            print(")", end="")


ex19()
