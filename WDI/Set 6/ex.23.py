# 23. We have given array T[N] which contains integers describing resistance of "n" resistors. Write function checking
# whether we can obtain equivalent resistance by combining in any way three random resistors.
# Solution: firstly, we recursively find a subset of three resistors. Later we can consider each of eights ways of
# combining three resistors and if any of them will generate an appropriate value we return true value.


def check(arr, value):
    # all three serially
    if arr[0] + arr[1] + arr[2] == value:
        return True
    # two serially and third one parallelly with them
    elif ((arr[0]+arr[1])*arr[2])/(arr[0]+arr[1]+arr[2]) == value:
        return True
    elif ((arr[0]+arr[2])*arr[1])/(arr[0]+arr[1]+arr[2]) == value:
        return True
    elif ((arr[1]+arr[2])*arr[0])/(arr[0]+arr[1]+arr[2]) == value:
        return True
    # two parallelly and third one serially with them
    elif (arr[0]*arr[1])/(arr[0]+arr[1]) + arr[2] == value:
        return True
    elif (arr[0]*arr[2])/(arr[0]+arr[2]) + arr[1] == value:
        return True
    elif (arr[1]*arr[2])/(arr[1]+arr[2]) + arr[0] == value:
        return True
    # three parallelly
    elif (arr[0]*arr[1]*arr[2])/(arr[0]*arr[1]+arr[1]*arr[2]+arr[0]*arr[2]) == value:
        return True


def ex23_reku(T, arr, index, k):
    if len(arr) == 3 and check(arr, k):
        return True
    if index < len(T):
        if ex23_reku(T, arr, index+1, k):
            return True
        if ex23_reku(T, arr+[T[index]], index+1, k):
            return True


def ex23(T, R):
    arr = []
    return ex23_reku(T, arr, 0, R)


T = [2, 2, 12, 13, 3, 16, 19]
print(ex23(T, 4))
