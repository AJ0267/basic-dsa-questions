# Sum of the numbers in a string.

def sum_of_numbers_in_string(string):
    total = 0
    current_number = ''
    
    for char in string:
        if char.isdigit():
            current_number += char  
        else:
            if current_number: 
                total += int(current_number)
                current_number = '' 

    if current_number:  
        total += int(current_number)

    return total