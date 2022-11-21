# 18. We have given two sequences with following relationship:
# A: a0 = 0, a1 = 1, an = an-1 - bn-1 * an-2
# B: b0 = 2, bn = bn-1 + 2 * an-1
# Write program, which reads integers from standard input and until they are not consecutive An sequence elements prints
# on standard output elements of the second sequence.
# Solution: we can easily solve this task using convenient python swap method with this time even five elements. When
# we pass to input wrong number program ends.

def cw18():
    a0, a1 = 0, 1
    b0 = 2
    b1 = b0 + (2 * a0)
    a2 = a1 - (b1 * a0)
    while int(input(">")) == a0:
        print(b0)
        a0, a1, b0, a2, b1 = a1, a2, b1, a1 - (b1 * a0), b0 + (2 * a0)


cw18()
