# 23. Determine number of nodes in a linked list cycle.
# Solution: I define two pointers that point to first node. One is moving every node and second one every second node.
# If they'll meet in one place it means that cycle exists. Then, I move one of these pointers and count number of nodes
# visited by it. When they'll meet again, total number of nodes visited by this pointer is a quantity of nodes in
# a linked list cycle.

class Node:
    def __init__(self):
        self.value = 0
        self.next = None


def tab2list(A):
    H = Node()
    C = H
    start = None
    for i in range(len(A)):
        X = Node()
        if i == 2:
            start = X
        X.value = A[i]
        C.next = X
        C = X
    C.next = start
    return H.next


def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


def ex23(A):
    slow, fast = A, A.next
    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    fast = fast.next
    ctr = 1
    while slow != fast:
        ctr += 1
        fast = fast.next
    return ctr


tab = [1, 2, 3, 4, 5, 6]
A = tab2list(tab)
print(ex23(A))
