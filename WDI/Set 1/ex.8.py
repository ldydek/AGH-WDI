# 8. Write program that checks if given number is prime.


def ex8(n):
    if n <= 1:
        return False
    s_u_m = 0
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            s_u_m += x + n//x
    if s_u_m == 0:
        return True
    return False


print(ex8(97))
