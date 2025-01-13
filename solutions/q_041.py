# Maximum and Minimum digit in a number.

def min_max_digit(num):
    num = sorted(str(num))
    return f"min > {int(num[0])}  \nmax > {int(num[-1])}"

print(min_max_digit(1020304050))