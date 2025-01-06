# Check whether a given number is positive or negative.

def positive_negative(number):
    if number > 0:
        return "Positive"
    elif number < 0 :
        return "Negative"
    else:
        return "Number is 0"
    

print(positive_negative(1))
print(positive_negative(-1))
print(positive_negative(0))

