# 03. Write a functions which merge two sorted linked lists into one sorted linked list. To these functions you should
# pass pointers to the first elements. Functions should return pointers to the newly created linked list.
# - iterative function
# - recursive function
# Solution: Iterative approach is very simple: we just compare values between two nodes and one of them we add to the
# new linked list. In that list where we choose added node from we move further and in the second one we stay at the
# same place. When one list will reach to the end we add remaining pieces to the new linked list.
# In a recursive approach we compare values between nodes and add node to the new linked list as well but this time we
# do a recursive call on the remaining sublists without added nodes and repeat the action.


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


def ex03_i(A, B):
    H = Node()
    J = H
    while A and B:
        if A.value < B.value:
            J.next = A
            J = J.next
            A = A.next
        else:
            J.next = B
            J = J.next
            B = B.next
    if A:
        J.next = A
    else:
        J.next = B
    return H.next


def ex03_r(A, B):
    H = Node()
    J = H
    ex03_recur(A, B, J)
    return H.next


def ex03_recur(A, B, J):
    if not A:
        J.next = B
        return
    elif not B:
        J.next = A
        return
    if A.value < B.value:
        J.next = A
        J = J.next
        ex03_recur(A.next, B, J)
    else:
        J.next = B
        J = J.next
        ex03_recur(A, B.next, J)


tab1 = [1, 2, 5, 8]
tab2 = [2, 5, 7, 10]
A = tab2list(tab1)
B = tab2list(tab2)
print_list(ex03_i(A, B))
