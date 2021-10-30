# 2. Write program checking whether given numbers are built with the same digits e.g. 123 and 312. I suppose here that
# 776661123 is built with digits: 7,6,1,2,3 and the same goes with 31276 (so repeats are not important).

def ex2(a, b):
    arr = [0]*10
    while a > 0:
        arr[a % 10] = 1
        a //= 10
    while b > 0:
        if arr[b % 10]:
            arr[b % 10] = 2
        else:
            return False
        b //= 10
    for x in range(10):
        if arr[x] == 1:
            return False
    return True


print(ex2(725, 2275))
# both numbers are built with 2, 5, and 7, so the answer is true
