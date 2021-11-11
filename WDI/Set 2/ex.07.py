# 7. Write program that for given natural number informs us whether it is a multiple of any sequence elements:
# An = n*n + n + 1.


def ex7(n):
    ctr, a = 1, 3
    while a < n and n % a:
        ctr += 1
        a = ctr*ctr + ctr + 1
    if n % a == 0:
        return True
    return False


print(ex7(785))
