# Check if a number is a Harshad number. 

def is_harshad(n):
    digit_sum = 0
    temp = n
    
    while temp > 0:
        digit_sum += temp % 10  # Add last digit to the sum
        temp = temp // 10  # Remove the last digit

    if n % digit_sum == 0:
        return True
    else:
        return False
    

print(is_harshad(18))