# Remove all duplicates from the input string. 

def remove_duplicates(string):
    unique = []
    for char in string:
        if char not in unique:
            unique.append(char)
    return "".join(unique)

print(remove_duplicates("Hello"))
