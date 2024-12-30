# Greatest of two numbers.

def greatest_of_two(a,b):
    if a > b :
        return f"a is greater than b"
    elif b > a:
        return f"b is greater than a"
    else:
        return f"a and b are equal"
    

print(greatest_of_two(20,20))