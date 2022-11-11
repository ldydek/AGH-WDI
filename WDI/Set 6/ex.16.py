# 16. Words are build with letters a...z. Two words have the same "weight" if they have the same quantity of vowels and
# ascii code sums of all letters in a single word are identical, for instance, "ula" -> 117,108,97 and "exe" -> 101,
# 120, 101. Write function "wyraz(s1,s2)", which checks if it is possible to build a word from letters from s2 (not all
# have to be included) and additionally this word must have the same "weight" as s1. Additionally function should
# return found word.
# Solution: at the beginning, we compute sum of ascii code of s1, number of vowels of s1 and create a list of single
# letter of s2. Now using recursion we try to build certain words that satisfies exercise conditions. If it is possible
# we return true, otherwise false.


# function that returns sum of all letters ascii code
def ascii_sum(string):
    count = 0
    for i in range(len(string)):
        count += ord(string[i])
    return count


# function that checks if given character is a vowel or not
def vowel(char):
    letters = ['a', 'e', 'i', 'o', 'u', 'y']
    return char in letters


# function that returns quantity of vowels in a given word
def vowels(string):
    ctr = 0
    for x in string:
        if vowel(x) is True:
            ctr += 1
    return ctr


# function that returns list of all letters that are present in a given string
def create_set(string):
    arr = []
    for x in string:
        if x not in arr:
            arr += [x]
    return arr


# recursive function
def wyraz_reku(weight, arr, vowels_ctr, vowels_number, word, solution):
    if weight == 0 and vowels_ctr == vowels_number:
        # if certain word was found we update one-element list that starts to keep final solution
        word[0] = solution
        return True
    for x in arr:
        if weight >= ord(x):
            if vowel(x) is True:
                if wyraz_reku(weight-ord(x), arr, vowels_ctr+1, vowels_number, word, solution+x):
                    return True
            else:
                if wyraz_reku(weight - ord(x), arr, vowels_ctr, vowels_number, word, solution+x):
                    return True


# main function
def wyraz(s1, s2):
    weight = ascii_sum(s1)
    arr = create_set(s2)
    vowels_ctr = 0
    vowels_number = vowels(s1)
    solution = ""
    word = [False]
    wyraz_reku(weight, arr, vowels_ctr, vowels_number, word, solution)
    return word[0]


print(wyraz("ula", "ipsca"))
