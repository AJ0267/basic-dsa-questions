# Write a program to find a word in a given string which has the highest number of repeated letters. 

def highest_repeats(s):
    words = s.split()
    max_repeats = 0
    result_word = ""
    
    for word in words:
        counts = {}
        repeat_count = 0
        
    for char in word:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
        
        for count in counts.values():
            if count > repeat_count:
                repeat_count = count
        
        if repeat_count > max_repeats:
            max_repeats = repeat_count
            result_word = word
    
    return result_word, max_repeats

print(highest_repeats("hello there"))
