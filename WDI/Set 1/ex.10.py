# 10. Print all perfect numbers smaller than million.


def is_perfect(k):
    suma, i = 0, 2
    while i**2 < k:
        if k % i == 0:
            suma += i + k//i
        i += 1
    suma += 1
    if int(k**(1/2)) == k**(1/2):
        suma += int(k**(1/2))
    if suma == k:
        return True
    return False


def ex10():
    for x in range(2, 10**6):
        if is_perfect(x):
            print(x, end=" ")


ex10()
