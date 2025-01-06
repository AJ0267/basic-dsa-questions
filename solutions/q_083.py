# Calculate frequency of characters in a string. 

def calc_freq(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1  
    return freq

print(calc_freq("hello"))
