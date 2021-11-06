# 19. Write program computing value of "e" number using: e = 1/0! + 1/1! + 1/2! + 1/3! + ... .
# Solution: I sum first 100 elements of this sequence to compute "e" value. Note that here simultaneously with adding
# new elements to the sum I can compute x! value, where "x" is a loop counter.

def ex19():
    a, factorial = 1, 1
    for x in range(1, 100):
        factorial *= x
        a += 1/factorial
    return a


print(ex19())
