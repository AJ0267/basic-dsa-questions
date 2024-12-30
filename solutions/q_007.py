#  Calculate sum of the elements of the array.

def sum_of_elements(arr):
    if len(arr) == 0:
        return None
    
    sum = 0
    for num in arr:
        sum += num

    return sum

arr = [20, 40, 80, 110]

print(sum_of_elements(arr))