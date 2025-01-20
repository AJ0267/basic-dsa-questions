# Remove duplicates from a sorted array. 

def remove_duplicates(arr):
    unique = []
    previous = None
    for num in arr:
        if num != previous:
            unique.append(num)
        previous = num
    return unique

arr = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7]
print(remove_duplicates(arr))