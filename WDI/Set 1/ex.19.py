# 19. Write program computing value of "e" number using: e = 1/0! + 1/1! + 1/2! + 1/3! + ... .

def ex19():
    a, factorial = 1, 1
    for x in range(1, 100):
        factorial *= x
        a += 1/factorial
    return a


print(ex19())
