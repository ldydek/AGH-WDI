# 11. Write program that informs us whether digits of given number create an increasing sequence.

def ex11(n):
    while n > 0:
        x = n % 10
        n //= 10
        if n % 10 >= x:
            return False
    return True


print(ex11(166))
