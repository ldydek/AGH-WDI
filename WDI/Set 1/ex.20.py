# 20. Given two sequences: An+1 = sqrt(An * Bn) and Bn+1 = (An + Bn)/2. They are convergent to the common limit called
# arithmetic-geometric mean. Write program computing this mean.
# Solution: During while loop action I assign constantly new values to the variables and when given accuracy is gained
# I can just return either "an" or "bn", because these values are almost the same.

def ex20():
    an, bn = 24, 6
    while abs(an-bn) > 10**(-10):
        x = an
        an = (an*bn)**(1/2)
        bn = (x+bn)/2
    return an


print(ex20())
