# 11. There is given array T[N]. Write function computing quantity of "n" numbers which product is equal to "k".
# Solution: I move from the end of the array (alternatively from the beginning) and when I find a number that is
# divisible by "k" I call a function recursively, but this time I look for product k // T[index]. When product becomes
# 1 I can increment variable that counts quantity of appropriate "n" numbers.

def ex11(T, k, n, index):
    quantity = 0
    if k == 1 and n == 0:
        quantity = 1
    for x in range(index, -1, -1):
        if k % T[x] == 0:
            quantity += ex11(T, k//T[x], n-1, x-1)
    return quantity


T = [1, 2, 6, 12]
print(ex11(T, 12, 3, len(T)-1))
# Answer: 1 - (1*2*6); n=3
