# 3. Chessboard is represented as a 2d array with natural numbers. Each number describes a cost of staying on a certain
# field. At the beginning, chess king is in a first row (accurate indexes are given in the input). It has to move to
# the last row in only 7 moves (we suppose that chessboard is a matrix T[8][8]). Write program that computes the
# cheapest path from given position to the last row. To the solution we also include cost of the first position and
# the last one.
# Solution: Chess king has always three possible moves: left-down, down or right-down, because number of its moves is
# limited to 7. So we can solve this problem by building recursive tree and temporary cost of the cheapest path keep
# in additional variable and update it if it's necessary.

from random import randint
# this module helps generate pseudorandom numbers


def ex03(arr, k):
    def ex03_recu(arr, x, k, suma):
        nonlocal solution
        # nonlocal variable has also access to external function (it's really useful when you don't want certain
        # variable be modified by a recursion, because our goal here is to update it when it's necessary)
        suma += arr[x][k]
        if x == len(arr) - 1:
            solution = min(solution, suma)
            return
        for y in range(max(k-1, 0), min(k+2, len(arr))):
            ex03_recu(arr, x+1, y, suma)
    solution = 10**10
    ex03_recu(arr, 0, k, 0)
    return solution


arr = [[randint(1, 100) for _ in range(8)] for _ in range(8)]
for x in range(len(arr)):
    for y in range(len(arr)):
        print(arr[x][y], end="  ")
    print()
print(ex03(arr, 2))
# firstly I want to show entire chessboard and later problem solution
