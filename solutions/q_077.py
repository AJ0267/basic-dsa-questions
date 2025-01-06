# Remove spaces from a string. 

def remove_spaces(string):
    spaces_removed = ''
    for char in string:
        if char != " ":
            spaces_removed += char
    return spaces_removed
print(remove_spaces("l o l     o        l "))
