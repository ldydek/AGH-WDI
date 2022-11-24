# 03. On a chessboard with dimensions 100 x 100 we place "n" queens (n < 100). Their positions are described by the
# list data = [(w1, k1), (w2, k2), (w3, k3),...,(wn, kn)]. Write a function which answers for the question if all queen
# pairs in that list don't check each other? To the function you should pass queens positions.
# Solution: I compare each pair of queens and check whether they have the same first or second index. Additionally, we
# have to check whether differences between respective indexes are the same or maybe sum of first queen indexes has the
# same value as second queen indexes. If one condition from that is satisfied it means that these queens check each
# other.


def ex03(data):
    n = len(data)
    for x in range(n):
        for y in range(x+1, n):
            # the same row
            if data[x][0] == data[y][0]:
                return False
            # the same column
            elif data[x][1] == data[y][1]:
                return False
            # the same diagonal
            elif data[x][0] - data[x][1] == data[y][0] - data[y][1] or data[x][0] + data[x][1] == data[y][0] + data[y][1]:
                return False
    return True


data = [(1, 2), (3, 3), (4, 0)]
print(ex03(data))
