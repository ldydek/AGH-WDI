# 22. Linked list can be ended with a cycle. Write function checking if it is true.
# Solution: I declare two pointers. One is visiting every node and the second one every second node. If faster node
# will reach the end it means that there is no cycle. On the other hand, if they will start pointing by reference to the
# same node, it means that cycle truly exists.

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


def ex22(A):
    slow, fast = A, A.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


tab = [1, 2, 3, 4, 5, 6]
A = tab2list(tab)
print(ex22(A))
