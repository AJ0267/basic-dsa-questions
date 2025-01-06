# Capitalize first and last character of each word. 

def capitalize_first_last(string):
    words = string.split()
    result = []
    for word in words:
        if len(word) > 1:
            new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            new_word = word.upper()
        result.append(new_word)
    return " ".join(result)

print(capitalize_first_last("hello how are you"))