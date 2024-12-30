# Leap year or not.

# Divisible by 4.
# Not divisible by 100 (unless...).
# Divisible by 400.

def leap_or_not(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Not leap year"
        else:
            return "Leap year"
    else:
        return "Not leap year"
    


print(leap_or_not(2021))