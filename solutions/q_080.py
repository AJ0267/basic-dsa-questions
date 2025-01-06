# Remove brackets from an algebraic expression. 

def remove_brackets(string):
    string_without_opening = string.replace('(', '')
    string_without_closing = string_without_opening.replace(')', '')

    return string_without_closing

print(remove_brackets('(3x + 1) = (3x - 1)'))