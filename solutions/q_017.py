# Maximum product subarray in an array. 

def max_product_subarray(arr):
    if not arr:
        return 0

    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]
    
    for i in range(1, len(arr)):
        num = arr[i]
        if num < 0:
            temp = max_prod
            max_prod = min_prod
            min_prod = temp

        if num * max_prod > num:
            max_prod = num * max_prod
        else:
            max_prod = num
        
        if num * min_prod < num:
            min_prod = num * min_prod
        else:
            min_prod = num
        
        if max_prod > result:
            result = max_prod
    return result

arr = [2, 3, -2, 4, -1, -2, 1, 5, -3, 2]
print(max_product_subarray(arr))
