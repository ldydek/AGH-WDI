# 18. We have a given array with natural numbers. Write program which computes the length of the longest contiguous
# subsequence which is a palindrome. Additionally, this palindrome can contain only odd numbers.
# Solution: Firstly, I consider possible palindromes with odd length, later with even.

def ex18(arr):
    n, solution = len(arr), 0

    for x in range(1, n-1):
        if arr[x] % 2:
            a, b = x-1, x+1
            ctr = 1
            while arr[a] == arr[b] and arr[a] % 2 and a >= 0 and b <= n-1:
                ctr += 2
                a -= 1
                b += 1
            solution = max(solution, ctr)

    for x in range(n-1):
        if arr[x] % 2 and arr[x] == arr[x+1]:
            a, b = x, x + 1
            ctr = 0
            while arr[a] == arr[b] and arr[a] % 2 and a >= 0 and b <= n-1:
                a -= 1
                b += 1
                ctr += 2
            solution = max(solution, ctr)
    if solution == 1:
        return 0
    return solution


arr = [1, 5, 5, 1, 10, 3, 1]
print(ex18(arr))
# Here answer is 4, because [1, 5, 5, 1] is a palindrome and we won't find any longer palindrome.
