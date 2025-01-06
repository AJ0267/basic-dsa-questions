# Remove characters from first string present in the second string. 

def remove_same_char(string1, string2):
    result = ""
    for char in string1:
        if char not in string2:
            result += char
    return result
            

print(remove_same_char("hello", "efg"))