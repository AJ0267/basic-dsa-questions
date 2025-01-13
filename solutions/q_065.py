def octal_to_binary(octal):
    octal_to_binary_map = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }

    binary = ""
    for digit in str(octal):
        binary += octal_to_binary_map[digit]

    return binary


print(octal_to_binary(0))