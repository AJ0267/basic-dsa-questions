# Permutations in which N people can occupy R seats in a classroom. 

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def permutations(n, r):
    if n < r:
        return 0 
    return factorial(n) // factorial(n - r)