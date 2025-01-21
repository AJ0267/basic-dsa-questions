# Convert octal to decimal. 

def octal_to_decimal(octal):
    decimal = 0
    octal_str = str(octal) 
    length = len(octal_str)
    
    for i in range(length):
        decimal += int(octal_str[i]) * (8 ** (length - 1 - i))
    
    return decimal


print(octal_to_decimal(345))
