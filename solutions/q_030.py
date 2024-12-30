# Check if a number is armstrong number of not.


def is_armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    armstrong_sum = 0


    for digit in digits:
        digit_power = int(digit) ** num_digits
        armstrong_sum += digit_power
    
    return armstrong_sum == number


print(is_armstrong(153))