# Check if a number is palindrome or not. 

def is_palindrome(number):
    original_num = str(number)
    reversed_num = original_num[::-1]

    return original_num == reversed_num


def is_palindrome2(number):
    original_num = number 
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10

    return original_num == reversed_num

# First Iteration:
#     digit = 121 % 10
#     reversed_num = 0 * 10 + 1 → reversed_num = 1
#     number = 121 // 10

# Second Iteration:
#     digit = 12 % 10
#     reversed_num = 1 * 10 + 2 → reversed_num = 12
#     number = 12 // 10

# Third Iteration:
#     digit = 1 % 10
#     reversed_num = 12 * 10 + 1 → reversed_num = 121
#     number = 1 // 10

print(is_palindrome(333))
print(is_palindrome2(313))
