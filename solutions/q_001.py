# Find the smallest number in an array.

def find_smallest(arr):

    if not arr:
        return None
    
    smallest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
    
    return smallest


arr = [30, 25, 15, 40, 35, 20]

print(find_smallest(arr))