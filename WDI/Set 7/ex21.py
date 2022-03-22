# 21. We call contiguous nodes of a linked list with increasing values an increasing sublist. Write program deleting
# the longest increasing sublist from a given linked list. There is only one condition: length of the longest increasing
# sublist has to be unique.
# Solution: Every time I meet a new increasing sublist I point to the first element of it and count its length. If this
# length is the longest so far I use another pointer which will start pointing at beginning of this sublist. At the end,
# this variable will hold first node of the longest increasing sublist. Moreover, I use one more variable to determine
# if longest sublist has an unique length. If so, at the I can simply remove it knowing first element and its length.

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def tab2list(tab):
    n = len(tab)
    a = b = None
    for x in range(n):
        h = Node()
        h.value = tab[x]
        if not a:
            a = h
            b = h
        else:
            b.next = h
            b = b.next
    return a


def print_list(a):
    while a:
        print(a.value, end="->")
        a = a.next
    print("None")


def ex21(a):
    h = Node()
    h.next = a
    k, start = None, a
    solution, ctr = 1, 1
    pointer, final_pointer = a, a
    while True:
        if ctr > solution:
            solution = ctr
            k = True
            final_pointer = pointer
        elif ctr == solution:
            k = False
        if start.next is None:
            break
        if start.value < start.next.value:
            if ctr == 1:
                pointer = start
            ctr += 1
        else:
            ctr = 1
        start = start.next
    if k:
        start = h
        while start.next != final_pointer:
            start = start.next
        pointer = start
        for x in range(solution):
            pointer = pointer.next
        start.next = pointer.next
    return h.next


tab = [1, 2, 4, 7, 8, 3, 6, 7]
a = tab2list(tab)
print_list(ex21(a))
