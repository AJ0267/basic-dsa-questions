# Find the median of the given array.

def find_median(arr):
    arr.sort() 
    n = len(arr)
    if n == 0:
        return None
    middle_element = n // 2

    if n % 2 == 1:
        return arr[middle_element]  
    else:
        return (arr[middle_element - 1] + arr[middle_element]) / 2
    
my_list = [9,2,3,5,4,6,8,7,1]
print(find_median(my_list))