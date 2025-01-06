# Find non-repeating characters of a string. 

def non_repeating(string):
    freq = {}
    unique = []
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    for char in freq:
        if freq[char] == 1:
            unique.append(char)
    
    return unique

print(non_repeating("lol"))