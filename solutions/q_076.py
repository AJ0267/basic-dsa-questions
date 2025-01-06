# Remove all vowels from the string. 

def remove_vowels(string):
    final_string = ''
    for char in string:
        if char.lower() not in "aeiou":
            final_string += char
    return final_string

print(remove_vowels("hello"))

