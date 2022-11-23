# 05. Write a function which divides linked list elements into 10 lists according to last digit in "value" field. At the
# end, newly created list we have to merge into one linked list in which elements are sorted non-decreasingly according
# to the last digit in a "value" class field.
# Solution: I allocate new array that consists of 10 new node. According to the last digit in a "value" field we remove
# considering node from input linked list and add it to the new one. In other words we have 10 new linked lists and
# pointers to them are stored in an array. We can allocate one more array, because thanks to it we can fast add new
# node at the end of a certain linked list. Second array keeps pointers to the last elements in each linked list.
# After we traverse input linked list we just merge all of them which are non-empty.


class Node:
    def __init__(self):
        self.value = 0
        self.next = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


def ex05(a):
    # two arrays: one keeps pointer to the linked lists heads, second one to the linked lists tails
    aux_tab1 = [Node() for _ in range(10)]
    aux_tab2 = [None] * 10
    for x in range(10):
        aux_tab2[x] = aux_tab1[x]
    while a:
        aux_tab2[a.value % 10].next = a
        aux_tab2[a.value % 10] = aux_tab2[a.value % 10].next
        tmp = a
        a = a.next
        tmp.next = None
    back = 0
    while back < 10:
        front = back + 1
        # here in a while loop we look for first linked list after considering which is non-empty
        # has more nodes than one guardian
        while front < 10 and aux_tab1[front].next is None:
            front += 1
        if front < 10:
            aux_tab2[back].next = aux_tab1[front].next
        back = front
    return aux_tab1[0].next


tab = [13, 11, 2, 100, 27, 5, 46, 138, 21]
a = tab2list(tab)
print_list(ex05(a))
