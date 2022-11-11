# 13. Write program printing all possible integer divisions for its components. For instance, for number 4 it will be
# 4 = 1+1+1+1 = 1+1+2 = 2+2 = 3+1.
# Solution: I consider numbers from 1 to given number without its inclusion. If it is possible to subtract certain
# number "k" from our integer "n" I do so and make a recursive call on a number: "n"-"k". Note that this program
# generates integer divisions without repeating, so, for instance, sum 2+1+1 and 1+1+2 will print only once.

# thanks to "start" variable program is not able to take data from array that is located on the left from considering
# number
def ex13_reku(n, start, aux_tab, string):
    if n == 0:
        string = string[:len(string)-1]
        print(string)
    for x in range(start, len(aux_tab)):
        if n >= aux_tab[x]:
            ex13_reku(n-aux_tab[x], x, aux_tab, string+str(aux_tab[x])+"+")


def ex13(n):
    string = ""
    aux_tab = [x for x in range(n-1, 0, -1)]
    return ex13_reku(n, 0, aux_tab, string)


ex13(4)
