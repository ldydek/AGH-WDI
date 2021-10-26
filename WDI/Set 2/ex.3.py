# 3. Write program that informs us whether entered number is a palindrome and later whether it is a palindrome in
# binary number system.


def is_palindrome(n, k):
    number = 0
    for x in range(k):
        k -= 1
        number += ((n // (10**x)) % 10) * (10**k)
    return number == n
# Here we create additional number adding digits from beginning to the end. Finally, if these two numbers are equal
# it means that "n" is a palindrome.


def binary(n):
    number, ctr = 0, 0
    while n > 0:
        number *= 10
        number += n % 2
        n //= 2
        ctr += 1
    return number, ctr
# Note that this function starts showing proper digits from last nonzero element, but for determining if binary
# representation is a palindrome it's sufficient knowing additionally number of digits in binary system.


def length(n):
    ctr = 0
    while n > 0:
        n //= 10
        ctr += 1
    return ctr
# Function returning number of digits.


def ex3(n):
    k = length(n)
    print(is_palindrome(n, k))
    a, b = binary(n)
    print(is_palindrome(a, b))


ex3(121)
