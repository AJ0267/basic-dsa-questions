# Check if a number is a perfect number. 

def is_perfect(number):
    sum_of_divisors = 0 

    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor

    return sum_of_divisors == number

print(is_perfect(6))