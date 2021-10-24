# 20. Given two sequences: An+1 = sqrt(An * Bn) and Bn+1 = (An + Bn)/2. They are convergent to the common limit called
# arithmetic-geometric mean. Write program computing this mean.

def ex20():
    an, bn, e = 24, 6, 10**(-10)
    while abs(an-bn) > e:
        x = an
        an = (an*bn)**(1/2)
        bn = (x+bn)/2
    return an


print(ex20())
