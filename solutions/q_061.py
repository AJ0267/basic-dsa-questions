# Convert binary to decimal. 

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        power += 1
        binary //= 10
    return decimal


print(binary_to_decimal(1010))