# 1. We call a certain string multiple if we can create it by repeating "n" times other string with a length
# at least 1 e.g. ABCABCABC, AAAA, BCBCBCBC. We have an array containing various strings. Write a program which
# determines the length of the longest multiple string in that array or 0 if we don't find any multiple string.

def f(T):
    n = len(T)
    for x in range(1, n//2+1):
        if n % x == 0 and T == T[0:x]*(n//x):
            return len(T)
    return 0
# checking whether given string is multiple


def multi(arr):
    solution = 0
    for x in range(len(arr)):
        solution = max(solution, f(arr[x]))
    return solution


arr = ["ABCABC", "AAAA", "ABCAABCA", "BBAC"]
print(multi(arr))
