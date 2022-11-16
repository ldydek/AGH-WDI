# 17. Write function which deletes from a doubly linked list all nodes which values in a binary number system have odd
# quantity of digit 1.
# Solution: at the beginning, I create an additional node - guardian. It will help me to remove first node if necessary.
# Now I can traverse entire doubly linked list and if certain node value satisfies task condition, I move previous node
# pointer of considering element to the next node and next node pointer to the previous node.


# class which represents a single node
class Node:
    def __init__(self):
        self.value = 0
        self.prev = None
        self.next = None


# function changing python list to the linked list
def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        X.prev = C
        C = X
    return H.next


# function which prints entire linked list
def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


# function checking if in a binary number system integer has an odd quantity of digit 1
def binary(a):
    ctr = 0
    while a:
        if a % 2 == 1:
            ctr += 1
        a //= 2
    return ctr % 2 == 1


# main function
def ex17(a):
    guard = Node()
    guard.next = a
    a.prev = guard
    while a:
        if binary(a.value):
            a.prev.next = a.next
            a.next.prev = a.prev
        a = a.next
    return guard.next


tab = [14, 12, 13, 9, 7, 7, 7, 9, 9, 7, 9]
a = tab2list(tab)
print_list(ex17(a))
