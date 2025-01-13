# Convert binary to octal.

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        power += 1
        binary //= 10
    return decimal

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)


print(binary_to_octal(1101))