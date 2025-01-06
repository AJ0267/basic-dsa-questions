# Find all palindrome numbers in a given range.

def is_palindromes_in_range(a, b):
    palindrome_numbers = []
    for num in range(a, b):
        if str(num) == str(num)[::-1]:
            palindrome_numbers.append(num)
    
    return palindrome_numbers

print(is_palindromes_in_range(10, 50))