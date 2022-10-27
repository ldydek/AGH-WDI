# 14. Write program computing probability of situation in which from group of "n" random people at least two of them
# were born in the same day of the year. Determine probability values for "n" in range 20-40.
# Solution: Consider "n", for instance, 20. Now, the best way to compute given probability is to consider the opposite
# event that everyone was born in different day. At the end, from certain even we just subtract computed value. We
# repeat that action for every "n" in range 20-40.

def probability(index):
    count = 1
    for x in range(index):
        count *= (365-x) / 365
    return 1 - count


def ex14():
    aux_tab = [0] * 21
    for x in range(20, 41):
        aux_tab[x-20] = probability(x)
    return aux_tab


print(ex14())
