# 04. Write function reversing a linked list.
# Solution: We create three variables and they are traversing given linked list. In every node we change "next"
# attribute in a middle node to that in the back. Later, "back" jumps to "middle", "middle" to "front" and "front"
# to next node.


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


def ex04(A):
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


tab = [1, 10, 2, 3, 4, 2]
A = tab2list(tab)
print_list(A)
print_list(ex04(A))
