# Count number of words in a given string. 

def count_words(string):
    words = string.split()
    return len(words)

print(count_words("hello"))