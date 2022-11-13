# 11. Linked list contains non-repeating elements. Write a function which deletes node with a certain value from a list
# if it's present. Otherwise it has to add it to the list.
# Solution: I traverse given linked list constantly having one additional pointer ("back) after main pointer ("front").
# It will help me to add or delete a node, because information about what action to take we will get from front pointer.
# Note that in this solution we traverse the linked list only once.


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


def ex11(a, k):
    # allocating a guard will help if list contains only one element which values equals to "k"
    # (of course additional node is not necessary, we can handle with that problem in different ways, for instance,
    # add some "if" statements
    guard = Node()
    guard.next = a
    back, front = guard, a
    while front and front.value != k:
        back = front
        front = front.next
    # if front is None it means that this linked list doesn't contain a node with value "k"
    if not front:
        h = Node()
        h.value = k
        back.next = h
    # otherwise we simply delete that node
    else:
        back.next = front.next
    return guard.next


tab = [1, 3, 6, 2, 10, 7]
a = tab2list(tab)
print_list(ex11(a, 7))
