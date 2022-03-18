# 25. There is a linked list ended with a cycle. Write function returning pointer to the last element before a cycle.
# Solution: In ex24 function computed first element of a cycle, so this time we can allocate one more variable that
# will point to node just before beginning of a cycle.

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


def ex25(A):
    slow, fast = A, A
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow, back = A, None
    while slow != fast:
        back = slow
        slow = slow.next
        fast = fast.next
    return back


tab = [1, 2, 3, 4, 5, 6]
A = tab2list(tab)
print(ex25(A))



