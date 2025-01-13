# Print Fibonacci up to Nth term. 

def fibonacci(n):
    a = 0
    b = 1
    fibonacci_sequence = [] 
    for _ in range(n):
        fibonacci_sequence.append(a) 
        temp = a
        a = b
        b = temp + b  
    return fibonacci_sequence 

print(fibonacci(10))