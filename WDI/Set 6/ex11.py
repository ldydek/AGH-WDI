# 11. There is given array T[N]. Write function computing quantity of "n" numbers which product is equal to "k".
# Solution: I move from the end of the array (alternatively from the beginning) and when I find a number that is
# divisible by "k" I call a function recursively, but this time I look for product k // T[index]. When product becomes
# 1 I can increment variable that counts quantity of appropriate "n" numbers.

def ex12(T, k, index):
    quantity = 0
    if k == 1:
        quantity += 1
    for x in range(index, -1, -1):
        if k % T[index] == 0:
            quantity += ex12(T, k//T[index], index-1)
    return quantity


T = [1, 2, 6, 12]
print(ex12(T, 12, len(T)-1))
# Answer: 4 - (1*2*6, 2*6, 1*12, 12)
