# Replace all 0s with 1s in a given integer.

def replace_zero_with_one(num):
    return int(str(num).replace('0', '1'))

print(replace_zero_with_one(10000200000300))