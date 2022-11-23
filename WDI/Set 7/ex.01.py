# 01. Implement an integer set using linked list structure. Write three function checking whether:
# - element is in a set
# - inserting element to the set
# - removing element from a set


# class which represents a single node
class Node:
    def __init__(self):
        self.value = 0
        self.next = None


# initializing a linked list
def initialize(A):
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


# function checking whether element is in a set
def contain(a, key):
    while a:
        if a.value == key:
            return True
        a = a.next
    return False


# function inserting new element to the set if it is not present inside
def insert(a, key):
    if contain(a, key):
        return
    node = Node()
    node.value = key
    while a.next:
        a = a.next
    a.next = node


# function removing element from a set
def remove(a, key):
    start = a
    if contain(a, key) is False:
        return
    if a.value == key:
        return a.next
    while a.next.value != key:
        a = a.next
    a.next = a.next.next
    return start


# main function
def ex01():
    a = initialize(tab)
    print_list(a)
    print(contain(a, 60))
    insert(a, 60)
    print_list(a)
    a = remove(a, 1)
    print_list(a)


tab = [1, 7, 10, 2, 3, 6]
ex01()
