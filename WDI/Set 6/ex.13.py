# 13. Write program printing all possible integer divisions for its components. For instance, for number 4 it will be
# 4 = 1+1+1+1 = 1+1+2 = 2+2 = 3+1.
# Solution: I consider numbers from 1 to given number with its inclusion. If it is possible to subtract certain number
# "k" from our integer "n" I do so and make a recursive call on a number: n-k.

def ex13(number, string):
    if number == 0:
        string = string[:len(string)-1]
        print(string)
    for i in range(1, number+1):
        ex13(number-i, string+str(i)+"+")


string = ""
ex13(4, string)
