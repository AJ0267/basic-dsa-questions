# Remove characters from a string except alphabets. 

def keep_alphabets(string):
    final_string = ""
    for char in string:
        if char.isalpha():
            final_string += char
    return final_string

print(keep_alphabets('abc1234bcbc566bcbcbc'))