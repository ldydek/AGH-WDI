# 24. There is a linked list ended with a cycle. Write function computing number of nodes before a cycle.
# Solution: I use technique with two pointers to determine a cycle. Now if I mark: x - number of nodes before a cycle,
# x+k - meeting point of two pointers, n - length of a cycle there is an equation 2*(x+k) = x+k+n, because faster node
# travelled twice more than slower one. Then we have, x = n - k. We move, for instance, slower pointer to the beginning
# and now two pointer travel with the same speed visiting every node. When they meet, they'll point for the first node
# of a cycle. At the end, we can travel linked list one more time from the beginning and count number of nodes until
# we won't be at the beginning of a cycle.

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
        if i == 4:
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


def ex24(A):
    slow, fast, ctr = A, A, 0
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = A
    while slow != fast:
        slow = slow.next
        fast = fast.next
    slow = A
    while slow != fast:
        ctr += 1
        slow = slow.next
    return ctr


tab = [1, 2, 3, 4, 5, 6]
A = tab2list(tab)
print(ex24(A))



