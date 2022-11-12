# 9. We have non-empty linked list which represents an integer. Consecutive nodes store consecutive integer digits.
# Write a function which increments this number.
# Solution: At the beginning, we reverse nodes order. Now if first node (last integer digit) has a value different than
# 9 we simply increment its value, reverse nodes order and finish a program. Otherwise, it has a 9 value and we are
# forced to traverse the linked list and look for first element which doesn't have a value 9. We increment the first
# node we meet with this condition. But when we traverse entire linked list it means that it consists only with digits
# equal to 9. In that case, we are forced to allocate new node with value 1 and add it to the linked list. At the end,
# we reverse nodes order once again.

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


# function reversing nodes order
def reverse(A):
    if not A:
        return None
    elif not A.next:
        return A
    back = None
    middle = A
    front = A.next
    while front:
        middle.next = back
        back = middle
        middle = front
        front = front.next
    middle.next = back
    return middle


# main function
def ex09(a):
    a = reverse(a)
    front = a
    back = None
    while front and front.value == 9:
        back = front
        front.value = 0
        front = front.next
    if front:
        front.value += 1
    else:
        H = Node()
        H.value = 1
        back.next = H
    a = reverse(a)
    return a


tab = [9, 9, 9]
a = tab2list(tab)
print_list(ex09(a))
