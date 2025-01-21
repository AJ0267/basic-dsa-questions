# Program to add two fractions. 

def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def add_fractions(num1, denom1, num2, denom2):
    result_num = num1 * denom2 + num2 * denom1
    result_denom = denom1 * denom2

    common_gcd = gcd(result_num, result_denom)
    result_num //= common_gcd
    result_denom //= common_gcd
    return result_num, result_denom

print(add_fractions(1,4,1,6))