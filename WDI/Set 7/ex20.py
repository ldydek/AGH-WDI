# 20. There is a given list of closed intervals. Write function reducing number of elements in a linked list. In other
# word we can change [2, 5] and [3, 6] intervals to [2, 6], because they intersect.
# Solution: Firstly, I sort given linked list by the first element. Later I do a linear traverse and if two contiguous
# intervals intersect I change value of the next one to minimum of two beginning values and maximum of two ending
# values. If not, I can change pointer from previous element (at the beginning it is a guardian) to first element of
# a pair in which two intervals don't intersect. I repeat this action until I traverse entire linked list.

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def intersection(a, b):
    if b.value[0] < a.value[0]:
        a, b = b, a
    if a.value[1] < b.value[0]:
        return False
    return a.value[0], max(a.value[1], b.value[1])


def tab2list(tab):
    a = b = None
    for x in range(len(tab)):
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


def ex20(a):
    a = bubble_sort(a)
    H = Node()
    b = H
    back, front = a, a.next
    while front:
        while front and intersection(back, front):
            start, stop = intersection(back, front)
            front.value = start, stop
            back = back.next
            front = front.next
        b.next = back
        b = b.next
        back = front
        if front:
            front = front.next
    return H.next


def length(a):
    ctr = 0
    while a:
        ctr += 1
        a = a.next
    return ctr


def bubble_sort(T):
    if T.next is None:
        return T
    ctr = length(T)
    for x in range(ctr):
        back = T
        middle = T.next
        front = T.next.next
        if back.value > middle.value:
            middle.next = back
            back.next = front
            curr = middle
            middle = back
            back = curr
            T = back
        while front:
            if middle.value > front.value:
                middle.next = front.next
                back.next = front
                front.next = middle
                curr = middle
                middle = front
                front = curr
            back = back.next
            middle = middle.next
            front = front.next
    return T


tab = [(15, 19), (2, 5), (7, 11), (8, 12), (5, 6), (13, 17)]
a = tab2list(tab)
print_list(ex20(a))
