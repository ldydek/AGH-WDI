# Solution: I start from the beginning of the list, take first element and consider all 4 possible three numbers that
# satisfies task condition (at most one space between two elements of certain three). After considering these cases
# I move to the second element and repeat the action.
# Attention! If you look for attached tests there is an assumption that gcd(a,b,c) = max(gcd(a,b),gcd(a,c),gcd(b,c))
# so, for instance, gcd(2,3,4) would be 2.

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# function for finding GCD of three numbers
def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)


def trojki(T):
    n = len(T)
    solution = 0
    for x in range(n-2):
        # possible cases
        # note that in some cases we could leave the list so we have to prevent from this situation
        if gcd_three(T[x], T[x+1], T[x+2]) == 1:
            solution += 1
        if x + 3 < n and gcd_three(T[x], T[x+1], T[x+3]) == 1:
            solution += 1
        if x + 3 < n and gcd_three(T[x], T[x+2], T[x+3]) == 1:
            solution += 1
        if x + 4 < n and gcd_three(T[x], T[x+2], T[x+4]) == 1:
            solution += 1
    return solution


T = [2, 3, 4, 5, 6, 8, 7]
print(trojki(T))
