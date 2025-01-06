# Count number of vowels, consonants, spaces in string.  

def count_of_all(string):
    counts = {'spaces': 0, 'vowels': 0, 'consonants': 0}
    for char in string:
        if char == " ":
            counts['spaces'] += 1 
        elif char.lower() in "aeiou" and char.isalpha():
            counts['vowels'] += 1 
        elif char.isalpha():
            counts['consonants'] += 1
    return counts

print(count_of_all("hello there, how are you?"))