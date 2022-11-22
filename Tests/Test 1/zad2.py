# 2. We have a given T[N][N] array with 0-1 values. We can treat each row as a number written in a binary system
# which consists of "N" bits. Maximum "N" value can be 100. Write "distance(T)" function, which will determines
# distance between two rows for which difference of numbers is the biggest. We can suppose that each row is a unique
# number.
# Solution: We can easily compare two binary numbers to determine which is bigger. The idea is to start from the
# beginning and compare digits on a certain position. When these digits become distinct bigger is that number in which
# we still have 1 (something similar happens in our decimal system that we are accustomed to). In this way we can
# compare every row with temporary the largest and lowest number and, at the end, compute the difference between
# indexes in a matrix to get final distance.


def relation(A, B):
    i = 0
    while A[i] == B[i]:
        i += 1
    if A[i] == 1:
        return True
    return False
# function to check which number (row) is bigger


def distance(T):
    n = len(T)
    m_i_n, m_a_x = 0, 0
    for x in range(1, n):
        if relation(T[x], T[m_a_x]):
            m_a_x = x
        elif relation(T[m_i_n], T[x]):
            m_i_n = x
    return abs(m_i_n - m_a_x)
# in "m_i_n" and "m_a_x" variables I keep temporary the biggest and smallest number (row) found so far


T = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1]]
print(distance(T))
