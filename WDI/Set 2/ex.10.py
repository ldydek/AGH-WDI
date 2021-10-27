# 10. Write program that informs us whether given number is a multiple of any sequence element: An = 3*A(n-1) + 1
# (recursive sequence) with the first element equal to 2. Note that we are forced to traverse in the worst case to the
# "n", because for "x", n//x don't have to be in a sequence (unlike for checking if given number is prime).

def ex10(n):
    a = 2
    while a < n and n % a:
        a = 3*a + 1
    if n % a == 0:
        return True
    return False


print(ex10(3456))
