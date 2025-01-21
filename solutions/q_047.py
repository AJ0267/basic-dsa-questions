# Check if a number is a strong number or not. 

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_strongnum(n):
    digits = str(n)
    sum_factorial = 0
    for digit in digits:
        sum_factorial += factorial(int(digit))
    return sum_factorial == n

num = 145
print(is_strongnum(num))

