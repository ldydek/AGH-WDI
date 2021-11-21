# 6. We have a given 1d array. Write program finding nonempty subset of this array elements for which sum of all
# numbers included is equal to their indexes from a list. We want to find a subset with minimum number of elements and
# program should return sum of all elements in that subset.
# Solution: Recursion is simple, because we have two possibilities. Either we include considered element in a subset
# or not. So we build binary recursive tree and thanks to additional variable that increments when an element is added
# we can easily find suitable subset. We have also two nonlocal variables that have access to external function and
# are not modified by recursion and we update them if we find appropriate subset with less quantity of elements.
# It's really important to understand why I return False in both cases. Answer is simple. I want to build entire
# binary recursive tree to consider all subsets. If I return True, for instance in second case, for same examples
# program can return subset with bigger quantity of elements (because suddenly one of function copies will return True
# and recursion will stop).


def ex06(arr):
    def ex06_recu(arr, sum1, sum2, i, ctr):
        nonlocal counter
        nonlocal solution
        if i < 0:
            return False
        if sum1 == sum2 and sum1:
            if ctr < counter:
                counter = ctr
                solution = sum1
            return False
        return ex06_recu(arr, sum1, sum2, i-1, ctr) or ex06_recu(arr, sum1+arr[i], sum2+i, i-1, ctr+1)
    counter, solution = len(arr), 0
    ex06_recu(arr, 0, 0, len(arr)-1, 0)
    return solution


arr = [1, 7, 3, 5, 11, 2]
print(ex06(arr))
