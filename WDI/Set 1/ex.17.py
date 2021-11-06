# 17. Write program computing the value which quotient of two Fibonacci sequence neighbouring elements approaches.
# Determine this quotient for different beginning elements of this sequence.
# Solution: During for loop running program prints quotient of two neighbouring elements. We can note that this
# quotient approaches to a certain number which is called golden number.


def ex17():
    a, b = 1, 1
    for x in range(300):
        print(b/a)
        a, b = b, a+b


ex17()
print((5**(1/2)+1)/2)
# golden number
