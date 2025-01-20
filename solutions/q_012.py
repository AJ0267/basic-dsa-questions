# Remove duplicates from unsorted array. 

def remove_duplicates(arr):
    unique = []
    seen = set() 
    for num in arr:
        if num not in seen:
            unique.append(num)
            seen.add(num) 
    return unique

arr = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7]
print(remove_duplicates(arr))