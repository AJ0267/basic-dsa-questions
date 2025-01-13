# Check if a number is Automorphic. 


def is_automorphic(num):
    num_square = num ** 2

    return str(num_square)[-len(str(num)):] == str(num)

print(is_automorphic(5))