# Check if the number is an abundant number or not. 


def is_abundant(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors > number:
        return True
    else:
        return False
    
print(is_abundant(12))
