# 02. Using functions from previous exercise write a function solving simultaneous equations of two equations with two
# unknowns.
# Solution: we solve that equations using determinants.

# function adding two fractions
def addition(a, b):
    return shortening((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))


# function subtracting two fractions
def subtraction(a, b):
    return shortening((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))


# function multiplying two fractions
def multiplication(a, b):
    return shortening((a[0] * b[0], a[1] * b[1]))


# function dividing fraction "a" by fraction "b"
def division(a, b):
    return shortening((a[0] * b[1], a[1] * b[0]))


# function raising a number to a nth power
def power(a, n):
    return shortening((a[0] ** n, a[1] ** n))


# function checking whether two fractions are equal
def equal(a, b):
    return a[0] * b[1] == a[1] * b[0]


# function returning greatest common divisor of two integers
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# function shortening certain fraction
def shortening(a):
    g_c_d = gcd(a[0], a[1])
    return a[0]//g_c_d, a[1]//g_c_d


# enter numbers separated by / e.g. 2/3
def fraction_input(statement):
    l, m = input(statement).split("/")
    l = int(l)
    m = int(m)
    l, m = shortening((l, m))
    return l, m


def ex02():
    a = fraction_input("a = ")
    b = fraction_input("b = ")
    c = fraction_input("c = ")
    d = fraction_input("d = ")
    e = fraction_input("e = ")
    f = fraction_input("f = ")

    W = subtraction(multiplication(a, e), multiplication(d, b))
    WX = subtraction(multiplication(b, f), multiplication(c, e))
    WY = subtraction(multiplication(a, f), multiplication(c, d))

    if W == 0:
        print("Equation does not have exactly one solution!")
        return

    print(division(WX, W))
    print(division(WY, W))


ex02()
