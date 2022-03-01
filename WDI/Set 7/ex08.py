# 08. Write function deleting every second element.
# Solution: I move two pointers one slower and one faster. Slower is moving to every node and faster to every second.
# Then I can point "next" attribute in a slower node to None and jump to faster node. I repeat this action until
# I get at the end of a linked list.


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


def ex08(A):
    slow, fast = A, A
    while fast and fast.next:
        fast = fast.next.next
        slow.next = fast
        slow = fast
    return A


tab = [1, 3, 2, 6, 7, 3, 1]
A = tab2list(tab)
print_list(A)
print_list(ex08(A))
