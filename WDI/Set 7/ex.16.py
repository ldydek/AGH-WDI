# 16. Write function which moves to the front these nodes which values in octal number system have even quantity of
# digit 5.
# Solution: at the beginning, I allocate additional node - guardian. This time it will be the beginning of a new linked
# list containing all these node which should be in the front. When I add certain element to the new linked list,
# I remove it from the original one. At the end, I merge these two linked lists.


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


# function checking if a certain number in octal number system has even quantity of digit 5
def octal(a):
    ctr = 0
    while a:
        if a % 8 == 5:
            ctr += 1
        a //= 8
    return ctr % 2 == 0


# function which obviously deletes node "b" from a linked list
def remove_node(a, b, c):
    a.next = c
    b = b.next
    if c:
        c = c.next


# main function
def ex16(a):
    start = a
    guard = Node()
    guard_jump = guard
    while start.next:
        if octal(start.next.value):
            # if condition is satisfied I add new node to the second linked list and remove it from the original one
            guard_jump.next = start.next
            guard_jump = guard_jump.next
            remove_node(start, start.next, start.next.next)
        else:
            start = start.next
    guard_jump.next = a
    return guard.next


# 13 and 69 have one digit 5 in octal number system, all others numbers have zero
tab = [13, 13, 15, 69, 6, 3, 4, 1, 9]
a = tab2list(tab)
print_list(ex16(a))
