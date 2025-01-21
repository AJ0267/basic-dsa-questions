# Print all prime factors of the given number. 

def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:
            factors.append(i) 
            if i != n // i:  
                factors.append(n // i)
    return sorted(factors) 

def prime_factors(n):
    factors = find_factors(n)
    prime_list = []  
    for factor in factors:  
        if is_prime(factor): 
            prime_list.append(factor) 
    return prime_list

num = 512
print(prime_factors(num))
