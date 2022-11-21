# 16. Smith's number is a composite number which sum of all digits is equal to sum of all numbers digits that are
# presented in its factorization. Write program that finds all these numbers smaller then one million.
# Solution: in the main faction I compare described above these two sums. If they are equal we can simply print that
# number as a Smith's number.


# function computing sum of all numbers digits in factorization
def smiths_number(n):
    if prime(n):
        return 0
    d, suma = 2, 0
    while n > 1:
        while n % d == 0:
            suma += sum_of_digits(d)
            n //= d
        d += 1
    return suma


# function computing sum of all digits in a certain number
def sum_of_digits(n):
    suma = 0
    while n:
        suma += n % 10
        n //= 10
    return suma


# function checking if given number is prime
def prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True


# main function
def ex16():
    for x in range(2, 10**6):
        if smiths_number(x) == sum_of_digits(x):
            print(x)


ex16()
