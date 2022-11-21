# 32. List represents polynomial with integer coefficients. Elements are ordered by growing powers (from the lowest to
# the greatest). Write a function computing difference between any two polynomials. Polynomials are represented by above
# described linked lists. Function should return a pointer to the newly created linked list. Previous ones should remain
# unchanged.
# Solution: because of the fact that elements are ordered by growing powers we have to reverse order of each linked list
# elements. After this we can simply make an addition from the biggest power to the lowest one. At the end, we "rewrite"
# these nodes which power is present only in one list and reverse order of a linked list elements.

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


# function reversing order of a linked list elements
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


# main function
def ex32(a, b):
    a = reverse(a)
    b = reverse(b)
    guard = Node()
    guard_jump = guard
    # making an addition
    while a and b:
        node = Node()
        node.value = a.value - b.value
        guard_jump.next = node
        guard_jump = guard_jump.next
        a = a.next
        b = b.next
    # if one of the linked lists still have elements we have to "rewrite" it so create new nodes with the same values
    while a:
        node = Node()
        node.value = a.value
        guard_jump.next = node
        guard_jump = guard_jump.next
        a = a.next
    while b:
        node = Node()
        node.value = b.value
        guard_jump.next = node
        guard_jump = guard_jump.next
        b = b.next
    guard = reverse(guard.next)
    return guard


tab1 = [1, 10, 3, 4, 6]
tab2 = [3, 20, 10]
a, b = tab2list(tab1), tab2list(tab2)
print_list(ex32(a, b))
