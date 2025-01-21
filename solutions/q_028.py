# Check if a number is prime or not.

def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number: #25 <= 11
        if number % i == 0 or number % (i+2) == 0:
            return False
        i+= 6
    return True

print(is_prime(11))