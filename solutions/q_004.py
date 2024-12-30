# Reverse a given array.

def reverse_array(arr):
    if not arr:
        return None
    
    return arr[::-1]

arr = [9,5,6,7,4]
print(reverse_array(arr))