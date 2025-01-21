# Check if Array is a subset of another array or not. 

def is_subset(arr1, arr2):
    arr1.sort() 
    arr2.sort()  

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]: 
            i += 1
        j += 1 

    return i == len(arr1)

arr1 = [3, 1, 5]
arr2 = [1, 2, 3, 4, 5, 6]
print(is_subset(arr1, arr2))  
