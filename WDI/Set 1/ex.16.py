# 16. There is a sequence of a given formula: An+1 = (An % 2) * (3 * An + 1) + (1 - An % 2) * An/2. Beginning from
# any natural number n > 1 one of the sequence elements will reach value 1 anyway. Write program finding starting
# element from range (2-10000) for which value 1 is accessible after greatest number of steps.
# Solution: I explicitly consider every number in range from 2 to 10000 and check for each one after how many steps
# value 1 will be accessible. Variables "solution" and "xd" keep information about best element and biggest number
# of steps found so far during for loop action.


def ex16():
    solution, xd = 0, 0
    for x in range(2, 10**4+1):
        an, steps = x, 0
        while an != 1:
            an = (an % 2) * (3 * an + 1) + (1 - an % 2) * (an/2)
            steps += 1
        if xd < steps:
            xd = steps
            solution = x
    return solution


print(ex16())
