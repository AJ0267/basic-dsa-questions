# Change case of each character in a string.  


def change_case(string):
    final_string = ''
    for char in string:
        if char.islower():
            final_string += char.upper()
        elif char.isupper():
            final_string += char.lower()
        else:
            final_string += char
    return final_string

print(change_case("Hello There, How Are You?"))