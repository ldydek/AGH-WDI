# 12. Modify previous program. This time it has to prints all found "n" numbers.
# Solution: All I need to do is to add additional array as a new function parameter. Now when I move further in
# a recursion tree I create entire new array with a new element at the end.

def ex12(T, k, n, index, aux_tab):
    quantity = 0
    if k == 1 and n == 0:
        print(aux_tab)
        quantity += 1
    for x in range(index, -1, -1):
        if k % T[x] == 0:
            quantity += ex12(T, k//T[x], n-1, x-1, aux_tab+[T[x]])
    return quantity


T = [1, 2, 6, 12]
aux_tab = []
n = 3
ex12(T, 12, n, len(T)-1, aux_tab)
