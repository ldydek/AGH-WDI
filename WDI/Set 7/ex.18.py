# 18. Write function which leaves in a linked list only nodes with unique values.
# Solution: at first, we allocate an additional node - guardian. It will help me to possibly delete first node if
# necessary. Now I traverse given linked list and each time we consider a new node I call an additional function which
# deletes nodes with the same values if there are more than 1.


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


# function which obviously deletes node "b" from a linked list
def remove_node(a, b, c):
    a.next = c
    b = b.next
    if c:
        c = c.next
    return a, b, c


# in this function we traverse given linked list and, at first, we delete nodes which have a value equal to the
# beginning node value
# if we delete only one node - this was at the beginning - it means that it was unique and we put it in its previous
# position, otherwise it wasn't unique and function deleted all these nodes before
def traverse(back, middle, front, value):
    ctr = 0
    link = middle
    b = back
    while middle:
        if middle.value == value:
            ctr += 1
            back, middle, front = remove_node(back, middle, front)
        else:
            back = back.next
            middle = middle.next
            if front:
                front = front.next
    if ctr == 1:
        middle = b.next
        b.next = link
        link.next = middle
        return b, True
    return b, False


# main function
def ex18(a):
    guard = Node()
    guard.value = float("-inf")
    guard.next = a
    back = guard
    middle = a
    front = a.next
    while front:
        # logic variable informs us whether previous node was unique, if so we move further with a pointers
        # otherwise after executing "traverse" function we do not move further, because now "back" pointer points to
        # the completely new node
        back, logic = traverse(back, middle, front, middle.value)
        middle = back.next
        front = middle
        if front:
            front = middle.next
        if logic is True:
            back = back.next
            middle = middle.next
            front = front.next
    return guard.next


tab = [100, 1, 6, 7, 2, 6, 7, 8, 4, 1, 1, 1]
a = tab2list(tab)
print_list(ex18(a))
