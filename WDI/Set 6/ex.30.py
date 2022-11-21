# 30. There are given two non-empty linked lists. Each linked list consists of different elements (in one linked list).
# In the first list elements are sorted increasingly, in the second one are in random order. Write a function which
# from these two lists will create one in which elements are sorted increasingly and make up union of two linked lists
# elements.
# Solution: I consider each element of a second list and check whether it is present in a first sorted list. If so,
# I simply move further. Otherwise we are forced to add it to this list. Allocating a guardian will help us to add
# certain node at the beginning.


# class which represents a single node
class Node:
    def __init__(self):
        self.value = 0
        self.next = None


# function changing python list to the linked list
def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


# function which prints entire linked list
def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


def add_node(back, front, node):
    back.next = node
    node.next = front


def ex30(a, b):
    guard = Node()
    guard.next = a
    while b:
        back, front = guard, guard.next
        while front and front.value < b.value:
            back = back.next
            front = front.next
        # note the here by allocating new variable "node" after adding a new node we still have access to the rest
        # of remaining unsorted list by variable "b"
        node = b
        b = b.next
        if front is None or front.value > node.value:
            add_node(back, front, node)
    return guard.next


tab1 = [2, 3, 5, 7, 11]
tab2 = [8, 2, 7, 4, 1, 100]
a, b = tab2list(tab1), tab2list(tab2)
print_list(ex30(a, b))
