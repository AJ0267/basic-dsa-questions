# Reverse digits of a number. 

def reverse_digits(number):
    num = str(number)
    if number < 0:
        reversed_num = "-" + num[:0:-1]
    else:
        reversed_num = num[::-1]
    
    return int(reversed_num)


print(reverse_digits(-200))


