# 31. Write a function which divides linked list into two linked lists. First one should contains keys even and
# positive, second one odd and negative, other keys should be removed from memory. To the function you should pass
# pointer to the list with data and pointers to the result lists. Function should returning quantity of removed nodes.
# Solution: I supposed here that list with data will be also a result list with even and positive keys. At first,
# I allocate two guardians for a result lists (it will help me, for instance, to remove first node or to add new nodes
# to the second list). Remaining nodes I can simply remove by moving pointers further in a linked list.

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


def ex31(a, guard2):
    guard1 = Node()
    guard1.next = a
    guard2_jump = guard2
    back, middle, front = guard1, a, a.next
    ctr = 0
    while middle:
        if middle.value % 2 == 0 and middle.value > 0:
            back = back.next
            middle = middle.next
            front = front.next
        elif middle.value % 2 == 1 and middle.value < 0:
            guard2_jump.next = middle
            guard2_jump = guard2_jump.next
            back, middle, front = remove_node(back, middle, front)
        else:
            ctr += 1
            back, middle, front = remove_node(back, middle, front)
    return guard2.next


tab = [3, -3, 6, -7, -2, 5, 10, -4, -5]
a = tab2list(tab)
print_list(ex31(a, Node()))

