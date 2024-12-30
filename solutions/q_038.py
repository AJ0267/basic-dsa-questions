# Greatest of three numbers.

def greatest_of_three(a,b,c):
    if a == b == c:
        return "a b c are equal"
    elif a >= b and a >=c :
        return "a is gretest"
    elif b >= a and b >= c:
        return "b is greatest"
    else:
        return "c is greatest"
                
print(greatest_of_three(1,1,2))