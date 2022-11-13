# 12. Set of strings is represented as a linked list. Strings are in alphabetical order in it. Write a function
# checking whether after adding certain string set cardinality will increase or not.
# Solution: we traverse given linked list and if we find the same string we simply return false value. Otherwise, thanks
# to two pointers ("back" and "front" - back pointer is following front one) we will have the following situation:
# back pointer points to a node with a string alphabetically smaller and front one to bigger or None value. In both
# cases we can put new node between them and point "back" to new node and new node to front pointer (possibly None).


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


def ex12(a, string):
    front = a
    guard = Node()
    guard.next = a
    back = guard
    # allocating a guard will help us to easily solve edge cases, for instance, adding string before list head
    while front and front.value <= string:
        # we found the same string - function returns false value
        if front.value == string:
            return False
        back = front
        front = front.next
    # if we reach this code it means that string is not present in a linked list
    # we add it and return true value
    h = Node()
    h.value = string
    back.next = h
    h.next = front
    return True


T = ["adaca", "cgav", "cgavb", "ctc", "xyz"]
a = tab2list(T)
print(ex12(a, "aaaa"))
