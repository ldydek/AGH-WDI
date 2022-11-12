# 06. Write function inserting at the end of the linked list new element.
# Solution: I traverse the list until "next" attribute will be None. It means that our variable points at the end
# of a list. Now we can create new node and set "next" attribute to that node.

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


def ex06(A, x):
    X = Node()
    X.value = x
    start = A
    while start.next:
        start = start.next
    start.next = X
    return A


tab = [1, 3, 2, 6, 7, 3]
A = tab2list(tab)
print_list(A)
print_list(ex06(A, 4))
