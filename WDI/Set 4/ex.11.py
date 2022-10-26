# 11. We call two numbers friends if they are built with the same digits. There is given 2d array filled with integers.
# Write function which computes all integers that are surrounded only by their friends.
# Solution: I traverse given matrix horizontally and thanks to auxiliary function I check if given integer is surrounded
# only by its friends.

def friends(a, b):
    aux_tab1 = [0] * 10
    aux_tab2 = [0] * 10
    while a:
        aux_tab1[a % 10] = 1
        a //= 10
    while b:
        aux_tab2[b % 10] = 1
        b //= 10
    for x in range(10):
        # if certain indexes are different it means that one digit occurs in certain integer and not in the other one
        if aux_tab1[x] != aux_tab2[x]:
            return False
    return True


def ex11(arr):
    n = len(arr)
    solution = 0
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
    # possible moves in a matrix
    for x in range(n):
        for y in range(n):
            flag = True
            for a, b in directions:
                if 0 <= x + a <= n-1 and 0 <= y + b <= n-1:
                    # this condition prevents from escaping outside of a given matrix
                    if friends(arr[x][y], arr[x+a][y+b]) is False:
                        flag = False
                        break
            if flag is True:
                solution += 1
    return solution


arr = [[166, 116, 13],
       [61, 6116, 116],
       [17, 611, 6611]]
print(ex11(arr))
