# 29. Two lists contain non-repeating integers (in one list). Elements in both linked lists are sorted increasingly.
# Write a function deleting from each list integers that are not present in a second one. Function should return number
# of deleted elements.
# Solution: in other words after deleting all appropriate elements we should get two same linked lists with elements
# that are present in both lists. So my idea was simple. At first, we compute lists lengths, later I add two guardians
# which help me to remove first elements if necessary. Now I can traverse first linked list and for each its elements
# look for node with the same value in second linked list. If it is present I change pointers in both linked lists to
# these nodes respectively. At the end, I compute number of deleted elements by comparing lengths of these linked lists
# before and after these operations.


class Node:
    def __init__(self):
        self.value = 0
        self.next = None


def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


# function which deletes node "b" from a linked list
def remove_node(a, b, c):
    a.next = c
    b = b.next
    if c:
        c = c.next
    return a, b, c


# function computing linked list length
def length(a):
    ctr = 0
    while a:
        ctr += 1
        a = a.next
    return ctr


def ex29(a, b):
    ctr1, ctr2 = length(a), length(b)
    guard1, guard2 = Node(), Node()
    guard1.next = a
    guard2.next = b
    back1, middle1, front1 = guard1, guard1.next, guard1.next.next
    ctr = 0
    list_jump_1 = guard1
    list_jump_2 = guard2
    while middle1:
        back2, middle2, front2 = guard2, guard2.next, guard2.next.next
        while middle2 and middle2.value < middle1.value:
            back2 = back2.next
            middle2 = middle2.next
            if front2:
                front2 = front2.next
        if middle2 and middle2.value == middle1.value:
            list_jump_1.next = middle1
            list_jump_1 = list_jump_1.next
            list_jump_2.next = middle2
            list_jump_2 = list_jump_2.next
            ctr += 2
        back1 = back1.next
        middle1 = middle1.next
        if front1:
            front1 = front1.next
    list_jump_1.next = None
    list_jump_2.next = None
    return ctr1 + ctr2 - 2*length(guard1.next)


tab1 = [1, 6, 10, 15, 16]
tab2 = [1, 5, 7, 15, 20, 30]
a, b = tab2list(tab1), tab2list(tab2)
print(ex29(a, b))
