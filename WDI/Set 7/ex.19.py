# 19. Elements in a linked list are ordered by their keys. Write function removing all nodes that don't have unique key.
# Solution: at the beginning, I allocate an additional node - guardian. It will help me to delete first element if
# necessary. Now I traverse entire linked list and use second internal loop to move front pointer to the first element
# after sequence of repeating values in nodes. If this sequence consists of only one element it means that node is
# unique and I move special pointer to that element (it moves only to the unique nodes). At the end, I move "next"
# field in a node of a special pointer to None, because if at the end of a linked list elements are not unique it will
# point to them.

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
    if b:
        b = b.next
    if c:
        c = c.next
    return a, b, c


def ex19(a):
    guard = Node()
    guard.next = a
    guard.value = float("-inf")
    # unique key
    jump = guard
    back = a
    front = a
    while back:
        ctr = 0
        while front and front.value == back.value:
            ctr += 1
            front = front.next
        # element is not unique
        if ctr > 1:
            back.next = front
            back = back.next
        # unique element
        else:
            jump.next = back
            jump = jump.next
            back = front
        jump.next = None
    return guard.next


tab = [1, 5, 5, 5, 2, 9, 9, 3, 3, 4, 8, 10]
a = tab2list(tab)
print_list(ex19(a))
