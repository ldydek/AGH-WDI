# 3. We have given a linked list that previously was an arithmetic sequence. Unfortunately, some nodes have been removed
# from it. Write a function repair(p) (p points to the first element) which fills given linked list with new elements
# to again obtain an arithmetic sequence. Function should return quantity of inserted elements. We can suppose that
# given linked list has more than 2 elements.
# Solution: firstly, we traverse given linked list and look for an arithmetic sequence difference as close to 0 as
# possible. Let's say it is "k". Later we traverse a linked list one more time and when difference between neighbouring
# nodes is not equal to "k" we start allocating new nodes until it is equal. When it finally will be equal to "k" we
# move further in a linked list until we reach the end.


# class which represents a single node
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# function changing python list to the linked list
def tab2list(A):
    H = Node("|")
    C = H
    for i in range(len(A)):
        X = Node(A[i])
        C.next = X
        C = X
    return H.next


# function which prints entire linked list
def print_list(A):
    while A:
        print(A.val, end="->")
        A = A.next
    print("None")


# main function
def repair(p):
    start = p
    r = p.next.val - p.val
    while start.next:
        tmp = start.next.val - start.val
        if tmp > 0:
            r = min(r, tmp)
        elif tmp < 0:
            r = max(r, tmp)
        else:
            r = 0
        start = start.next
    start = p
    while start.next:
        while start.next.val - start.val != r:
            node = Node(start.val+r)
            tmp = start.next
            start.next = node
            node.next = tmp
            start = start.next
        start = start.next
    return p


tab = [6, 4, 0]
a = tab2list(tab)
print_list(repair(a))
