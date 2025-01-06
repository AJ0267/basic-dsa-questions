# Check if a given string is palindrome or not.


def is_palindrome_string(string):
    return string == string[::-1]

print(is_palindrome_string("racecar"))