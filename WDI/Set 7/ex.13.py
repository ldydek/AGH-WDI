# 13. Write function which deletes all nodes which have a value lower than node value directly preceding considering
# node.
# Solution: at the beginning, I reverse nodes order. Now I can traverse given linked list once again and check if
# certain node value is lower than the next one. If so, I delete this node and move further. At the end, I reverse nodes
# order once again.


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


# function reversing nodes order
def reverse(A):
    if not A:
        return None
    elif not A.next:
        return A
    back = None
    middle = A
    front = A.next
    while front:
        middle.next = back
        back = middle
        middle = front
        front = front.next
    middle.next = back
    return middle


def ex13(a):
    a = reverse(a)
    guard = Node()
    # allocating a guard will help us delete first node if necessary
    guard.next = a
    back = guard
    middle = a
    front = a.next
    while front:
        if middle.value < front.value:
            back.next = front
            middle = front
            front = front.next
        else:
            back = back.next
            middle = middle.next
            front = front.next
    a = reverse(guard.next)
    return a


tab = [1, 10, 8, 9, 7, -6, 6, 8, -1]
a = tab2list(tab)
print_list(ex13(a))

