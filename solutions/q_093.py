# Write a program to find the largest word in a given string. 

def largest_word(string):
    words = string.split()
    print(words)

    largest_word = ""

    for word in words:
        if len(word) > len(largest_word):
            largest_word = word
    
    return largest_word

print(largest_word("how you doing"))