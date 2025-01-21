# GCD of two numbers.

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b 
    return a

print(gcd(12,15))

