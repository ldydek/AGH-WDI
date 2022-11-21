# 33. String s1 precedes string s2 if its last letter is "lower" then s2 first letter. According to this rule, various
# strings were placed in a circular linked list. Example: "bartek"->"leszek"->"marek"->"ola"->"zosia"->"bartek"->... .
# Write a function inserting to this list a new string if it is possible. To the function you should pass pointer to
# the linked list and inserting string. Function should returning logical value if we were able to insert a new string.
# After possible inserting pointer to the list should point on newly inserted element.
# Solution: firstly, I create a circular linked list. Now I can traverse this list only once and check whether inserting
# is possible. Note that I pass pointer to the linked list as a one-element array, because after executing the function,
# if inserting occurred, pointer to the list will change.

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
    C.next = H.next
    return H.next


# function which prints entire linked list
def print_list(A):
    while A:
        print(A.value, end="->")
        A = A.next
    print("None")


# adding a new node to the linked list
def add_string(start, string):
    node = Node()
    node.value = string
    front = start.next
    start.next = node
    node.next = front
    return node


# "flag" variable helps me to execute while loop at the beginning (do-while loop in other languages)
def ex33(a, string):
    start, flag = a[0], True
    while start != a[0] or flag:
        flag = False
        if start.value[-1] < string[0] and string[-1] < start.next.value[0]:
            a[0] = add_string(start, string)
            return True
        start = start.next
    return False


tab = ["bartek", "leszek", "marek", "olek", "zosia"]
a = [None]
a[0] = tab2list(tab)
print(ex33(a, "ala"))
