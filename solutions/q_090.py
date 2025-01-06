# Print all the duplicates in the input string. 

def all_duplicates(string):
    freq = {}
    duplicates = []

    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    for char in freq:
        if freq[char] > 1:
            duplicates.append(char)

    return duplicates

print(all_duplicates("hello"))
        