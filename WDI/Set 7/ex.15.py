# 15. Write function deleting all nodes that have values which represented in a ternary numeral system have more 1 than
# 2.
# Solution: At the beginning, I allocate additional node - guardian. It will help me to delete first element if
# necessary. Now I can traverse entire linked list and if certain node value satisfies task condition I simply delete
# it (call additional function which does it). Otherwise, I just move further.

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


# function checking if in a ternary representation integer has more 1 than 2
def ternary(a):
    ctr1, ctr2 = 0, 0
    while a:
        if a % 3 == 1:
            ctr1 += 1
        elif a % 3 == 2:
            ctr2 += 1
        a //= 3
    if ctr1 > ctr2:
        return True
    return False


# function which obviously deletes node "b" from a linked list
# after it is called pointer from "a" points directly to "c" ("b" node has no references)
def remove_node(a, b, c):
    a.next = c
    b = b.next
    if c:
        c = c.next


# main function
def ex15(a):
    guard = Node()
    guard.next = a
    a = guard
    while a.next:
        if ternary(a.next.value):
            remove_node(a, a.next, a.next.next)
        else:
            a = a.next
    return guard.next


tab = [13, 5, 8, 1, 2, 7, 3, 14, 8]
a = tab2list(tab)
print_list(ex15(a))
