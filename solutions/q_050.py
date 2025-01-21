# LCM of two numbers. 

#lcm without GCD.
def lcm(a, b):
    multiple = a * b
    for i in range(1, multiple + 1):
        if i % a == 0 and i % b == 0:
            return i
        
print(lcm(12, 15))

# lcm with GCD.

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b 
    return a

def lcm1(a, b):
    return (a * b) // gcd(a, b)

print(lcm1(12,15))



