# 13. Write program that informs us whether at the end of given number there is an unique digit.

def ex13(n):
    x = n % 10
    n //= 10
    while n > 0:
        if n % 10 == x:
            return False
        n //= 10
    return True


print(ex13(340))
