# 11. Write program computing all pairs of amicable numbers smaller than million. Amicable numbers means that sum
# of one number divisors, excluding the number itself equals to the second one and the same happens with another
# number of this pair.

def ex11():
    for x in range(2, 10**6):
        a = sum_of_proper_divisors(x)
        b = sum_of_proper_divisors(a)
        if x == b and x < a and b < 10**6:
            print((x, a))


def sum_of_proper_divisors(n):
    suma = 0
    for x in range(2, int(n**(1/2))+1):
        if n % x == 0:
            suma += x + n//x
    if int(n**(1/2)) == n**(1/2):
        suma -= int(n**(1/2))
    suma += 1
    return suma


ex11()
