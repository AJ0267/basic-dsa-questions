# Change every letter with the next lexicographic alphabet in the given string. 

def shift_letters(string):
    result = ''
    for char in string:
        if char.islower():
            if char == 'z':
                result += 'a'
            else:
                result += chr(ord(char) + 1)
        elif char.isupper():
            if char == 'Z':
                result += 'A'
            else:
                result += chr(ord(char) + 1)
        else:
            result += char
    return result

print(shift_letters('Hello World!'))