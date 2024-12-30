# Find the largest number in an array.

def find_largest(arr):
    if not arr:
        return None
    
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
    
    return largest

arr = [30, 15, 20, 25, 5, 10, 35]

print(find_largest(arr))