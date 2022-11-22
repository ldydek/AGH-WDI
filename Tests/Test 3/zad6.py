# Solution: I traverse first list and check whether considering element is present in second and third list thanks to
# auxiliary function called "find". If so, I move pointer of solution list node to that element. Solution list means of
# course this list which consists of elements that are present in lists z1, z2, z3. We can easily implement that
# solution having guardian at the beginning of the solution list. Note that here are also attached functions that help
# to check task correctness - "tab2list" and "print_list".

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def tab2list(A):
    H = Node(0)
    C = H
    for i in range(len(A)):
        X = Node(A[i])
        C.next = X
        C = X
    return H.next


def print_list(A):
    while A:
        print(A.val, end="->")
        A = A.next
    print("None")


def find(x, value):
    while x:
        if x.val == value:
            return True
        x = x.next


def iloczyn(z1, z2, z3):
    guard = Node(0)
    start = guard
    jump = z1
    while jump:
        if find(z2, jump.val) and find(z3, jump.val):
            start.next = jump
            start = start.next
        jump = jump.next
    start.next = None
    return guard.next


A = [1, 2, 3, 4]
B = [2, 3, 4, 7, 13]
C = [2, 3, 4, 6, 11]
a = tab2list(A)
b = tab2list(B)
c = tab2list(C)
print_list(a)
print_list(b)
print_list(c)
print_list(iloczyn(a, b, c))
