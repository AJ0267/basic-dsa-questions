# Program to find roots of a quadratic equation. 

def sqrt(num):
    if num < 0:
        return num ** 0.5
    return num ** 0.5

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    # +ve, 0, -ve
    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(abs(discriminant)) / (2 * a)
        return (real_part + imaginary_part, real_part - imaginary_part)
    

print(find_roots(1,-3,2))

