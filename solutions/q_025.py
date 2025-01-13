# Check if Array is a subset of another array or not. 

def is_subset(arr1, arr2):
    for element in arr2:
        if element not in arr1:
            return False
    return True


arr1 = [1, 2, 3, 4, 5]
arr2 = [6]
print(is_subset(arr1, arr2))