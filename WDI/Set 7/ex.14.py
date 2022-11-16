# 14. Write function deleting from a linked list all elements which values are divisible by their following nodes.
# Solution: at the beginning, I allocate an additional node (guard) for helping to possibly delete first element. Now
# I traverse given linked list and simply delete each node which has described properties.


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


def ex14(a):
    guard = Node()
    guard.next = a
    front = a.next
    middle = a
    back = guard
    while front:
        # divisible value so we are forced to delete this node
        if front.value % middle.value == 0:
            back.next = front
        else:
            # otherwise we simply move further
            back = back.next
        middle = middle.next
        front = front.next
    return guard.next


tab = [2, 4, 8, 11, 13, 5, 10, 20]
a = tab2list(tab)
print_list(ex14(a))
