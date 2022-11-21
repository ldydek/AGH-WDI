# 26. Write function checking whether one linked list is inside second one.
# Solution: at the beginning, I compute lengths of these two linked lists. If first one is longer I swap points to them.
# After that "a" pointer points always to a linked list not longer then second one. Now I traverse longer linked list
# and when certain element will have the same value as first node in a not longer list I use internal loop to check
# how long these linked lists will have the same values. If we traverse entire not longer list it means that the second
# one contains this one.


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


# function computing linked list length
def length(a):
    ctr = 0
    while a:
        ctr += 1
        a = a.next
    return ctr


# main function
def ex26(a, b):
    a_length = length(a)
    b_length = length(b)
    if a_length > b_length:
        a, b = b, a
    # now "a" points to shortest linked list and "b" to the longest one
    a_jump, b_jump = a, b
    while b_jump:
        while a_jump and a_jump.value == b_jump.value:
            a_jump = a_jump.next
            b_jump = b_jump.next
        if a_jump is None:
            return True
        a_jump, b_jump = a, b
        b = b.next
        b_jump = b_jump.next
    return False


tab1 = [8, 10]
tab2 = [1, 2, 8, 10, 10]
a = tab2list(tab1)
b = tab2list(tab2)
print(ex26(a, b))


