# Sum of digits of a number.


def sum_of_digits_loop(number):
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

def sum_of_digits_recursion(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits_recursion(number // 10)
    

print(sum_of_digits_loop(1234))
print(sum_of_digits_recursion(1234))