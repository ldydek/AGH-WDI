# 28. Two linked lists contain distinct numbers (within a list). In the first one elements are sorted increasingly and
# in the second one not. Write program deleting numbers occurring in these two lists.
# Solution: for every element I check if it also exists in the second list. If so, I delete these two nodes.


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


def ex28(a, b):
    # allocating guardians will help to remove first element if necessary
    h1 = Node()
    h2 = Node()
    h1.next, h2.next = a, b
    back1, middle1, front1 = h1, h1.next, h1.next.next
    ctr = 0
    while middle1:
        flag = False
        back2, middle2, front2 = h2, h2.next, h2.next.next
        while middle2:
            if middle1.value == middle2.value:
                flag = True
                back1, middle1, front1 = remove_node(back1, middle1, front1)
                # I still have a reference to removed node (middle) so I am forced to update above pointers
                remove_node(back2, middle2, front2)
                # updating these pointers is not necessary, because we do it at the beginning of a loop
                ctr += 2
                break
            back2 = back2.next
            middle2 = middle2.next
            if front2:
                front2 = front2.next
        if flag is False:
            back1 = back1.next
            middle1 = middle1.next
            if front1:
                front1 = front1.next
    return ctr


tab1 = [1, 4, 5, 7, 10]
tab2 = [4, 1, 30, 7, 10, 5, 40]
a = tab2list(tab1)
b = tab2list(tab2)
print(ex28(a, b))
