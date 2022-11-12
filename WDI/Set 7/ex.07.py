# 07. Write function deleting last element in a linked list.
# Solution: I traverse the list until I am next to last element. Now I can point "next" attribute to None and
# garbage collector will do the rest ;).

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


def ex07(A):
    start = A
    while start.next.next:
        start = start.next
    start.next = None
    return A


tab = [1, 3, 2, 6, 7, 3]
A = tab2list(tab)
print_list(A)
print_list(ex07(A))
