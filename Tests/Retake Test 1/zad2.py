# 2. We have given word which consists with letters from english alphabet. We cut this word into some pieces but each
# piece has to contain exactly one vowel. Write a function cutting(s), which returns number of ways of cutting this
# word.
# Examples:
# print(cutting(’student’)) returns 2, because stu-dent, stud-ent
# print(cutting(’sesja’)) returns 3, because se-sja, ses-ja, sesj-a
# print(cutting(’ocena’)) returns 8
# Solution: at the beginning, I traverse this word and mark in additional array places where we meet vowels. Later
# I call additional function which returns indexes on which we can meet first and last digit 1 in the array. At the end,
# we simply traverse this array one more time between these indexes and count how many 0 (how many consonants) is next
# to each other. We multiply length of that sequence with 0 by the "value" variable initialized at the beginning to 1.
# When we meet 1 we reset counter to 1 and repeat the action (combinatorial approach not recursive).
# Passed all tests


# function checking whether given character is a vowel
def vowel(arr, char):
    return char in arr


# function returning indexes on which there are first and last digit 1
def first_last(arr):
    n = len(arr)
    index1, index2 = 0, n-1
    while arr[index1] == 0:
        index1 += 1
    while arr[index2] == 0:
        index2 -= 1
    return index1, index2


# main function
def cutting(s):
    n = len(s)
    vowels = ["a", "ą", "e", "ę", "i", "o", "ó", "u", "y"]
    aux_arr = [0] * n
    index = 0
    for x in range(len(s)):
        if vowel(vowels, s[x]):
            aux_arr[x] = 1
            index += 1
    index1, index2 = first_last(aux_arr)
    value, ctr = 1, 1
    for x in range(index1+1, index2+1):
        if aux_arr[x] == 0:
            ctr += 1
        else:
            value *= ctr
            ctr = 1
    return value


print(cutting("informatyka"))


