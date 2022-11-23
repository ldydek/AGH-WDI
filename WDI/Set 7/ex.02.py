# 02. Using linked list to the array implementation. Write three functions:
# - initializing an array
# - returning value of an element at index "n"
# - inserting a new value to the node at index "n"


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


# returning value of an element at index "n"
def node_value(a, n):
    while a and n:
        a = a.next
        n -= 1
    return a.value


# inserting a new value to the node at index "n"
def insert(a, n, value):
    while a and n:
        a = a.next
        n -= 1
    a.value = value


def ex02():
    a = initialize(tab)
    print_list(a)
    print(node_value(a, 3))
    insert(a, 4, 100)
    print_list(a)


tab = [1, 5, 10, 2, 6, 40, 7]
ex02()
