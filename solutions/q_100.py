# Reverse words in a string. 

def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    result = " ".join(reversed_words)

    return result

print(reverse_words("how are you"))