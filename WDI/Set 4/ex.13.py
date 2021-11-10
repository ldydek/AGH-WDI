# 13. Natural numbers a, b are complementary when their sum is a prime number. There is a given 2d array with natural
# numbers. Write program which changes all elements that don't have complementary number to 0.
# Solution: For each element in an array I check sum with all numbers (apart from itself) and when it'll never be prime
# it means that this element doesn't have complementary number. If certain element was found we change its sign,
# because later we'll need absolute value of it for checking another element.
# "k" - logical value informing us whether we found prime sum of certain elements in a matrix
# "l" - logical value helping us break external loop (we don't have to check further unnecessarily if prime number was
# found)

def if_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


def ex13(arr):
    n = len(arr)
    for a in range(n):
        for b in range(n):
            k, l = True, True
            for c in range(n):
                for d in range(n):
                    if a == c and b == d:
                        continue
                    if if_prime(abs(arr[a][b]) + abs(arr[c][d])):
                        k, l = False, False
                        break
                if l is False:
                    break
            if k:
                arr[a][b] = -arr[a][b]
    for x in range(n):
        for y in range(n):
            if arr[x][y] < 0:
                arr[x][y] = 0
    return arr
# at the end searched numbers are negative so we can simply change them to 0


arr = [[1, 3, 5], [1, 10, 9], [5, 4, 3]]
print(ex13(arr))
