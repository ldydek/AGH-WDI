# 09. Same exercise as 08 but this time program has to print chosen weights not only inform if it's possible.
# If we change "return True" to e.g. "return False" or "return" we won't stop recursion earlier and program will show
# other solutions as well - it's good to know about it.

def ex09_recu(arr, k, i, A):
    if k == 0:
        print(A)
        return True
    if i < 0:
        return False
    if ex09_recu(arr, k, i-1, A) or ex09_recu(arr, k-arr[i], i-1, A+[arr[i]]) or ex09_recu(arr, k+arr[i], i-1, A+[arr[i]]):
        return True


arr = [1, 2, 5, 3]
ex09_recu(arr, 9, len(arr)-1, [])
