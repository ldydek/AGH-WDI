# 10. Integers are represented in the same way as in previous task (nodes are digits). Write a function adding certain
# two integers. As a result it should arise new linked list.
# Solution: I use written method to add two numbers. At the beginning, we have to reverse nodes order. Now we start to
# making an addition. If I traverse one list before another (one is shorter) I use additional loop to traverse the
# second one. After addition if we still have "value" variable equal to 1 it means that we are forced to allocate new
# node at the beginning and link it with the rest of the linked list. At the end, we reverse nodes order.

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


# function reversing nodes order
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


def ex10(a, b):
    a = reverse(a)
    b = reverse(b)
    start_a = a
    start_b = b
    guard = Node()
    front = guard
    value = 0
    while start_a and start_b:
        H = Node()
        H.value = (start_a.value + start_b.value + value) % 10
        value = (start_a.value + start_b.value + value) // 10
        front.next = H
        front = front.next
        start_a = start_a.next
        start_b = start_b.next
    while start_a:
        H = Node()
        H.value = (start_a.value + value) % 10
        value = (start_a.value + value) // 10
        front.next = H
        front = front.next
        start_a = start_a.next
    while start_b:
        H = Node()
        H.value = (start_b.value + value) % 10
        value = (start_b.value + value) // 10
        front.next = H
        front = front.next
        start_b = start_b.next
    if value == 1:
        H = Node()
        H.value = 1
        front.next = H
    guard = reverse(guard.next)
    return guard


tab1 = [7, 7, 9]
tab2 = [2, 9]
a = tab2list(tab1)
b = tab2list(tab2)
print_list(ex10(a, b))
