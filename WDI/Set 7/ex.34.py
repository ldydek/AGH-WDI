# 34. Write a function, which deletes from a circular linked list elements that occur in it exactly "k" times. To the
# function you should pass pointer to one of its elements and number "k". Function should return information whether
# some elements were deleted.
# Solution: at first, we remove a cycle from this list. Now for each node we count number of nodes which have the same
# value. If it is equal to "k" we remove all that nodes using additional function. But before doing it we have to
# move further in a linked list to the first node which does not have this value which was present "k" times. Otherwise,
# we'll lost access to the linked list.


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
    C.next = H.next
    return H.next


# function which prints entire linked list
def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


# function deleting a cycle from a linked list
def delete_cycle(a):
    start = a
    while start.next != a:
        start = start.next
    start.next = None


# function which deletes node "b" from a linked list
def remove_node(a, b, c):
    a.next = c
    b = b.next
    if c:
        c = c.next
    return a, b, c


# function which traverse linked list once and removes all node which have value equal to "key" variable
def remove_keys(guard, key):
    back, middle, front = guard, guard.next, guard.next.next
    while middle:
        if middle.value == key:
            back, middle, front = remove_node(back, middle, front)
        else:
            back = back.next
            middle = middle.next
            if front:
                front = front.next
    return guard


# main function
def ex34(a, k):
    delete_cycle(a)
    curr = a
    flag = False
    guard = Node()
    guard.next = a
    a = guard
    while curr:
        start = a.next
        ctr = 0
        while start:
            if start.value == curr.value:
                ctr += 1
            start = start.next
        val = curr.value
        while curr and curr.value == val:
            curr = curr.next
        if ctr == k:
            remove_keys(guard, val)
            flag = True
    return flag


tab = [10, 5, 8, 5, 2, 1, 5, 1]
a = tab2list(tab)
print(ex34(a, 3))
