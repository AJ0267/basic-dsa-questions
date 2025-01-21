# Factors of a given number. 

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:
            factors.append(i) 
            if i != n // i:  
                factors.append(n // i)
    return sorted(factors) 

num = 28
print(find_factors(num))
