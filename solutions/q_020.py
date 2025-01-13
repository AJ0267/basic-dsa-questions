# Rotation of elements of array - left and right. 

def rotate_array(arr, K, direction="left"):
    n = len(arr)
    K = K % n  #when K > n
    
    if direction == "left":
        print('left')
        arr[:K] = arr[:K][::-1]  # Reverse 0-K
        arr[K:] = arr[K:][::-1]  # Reverse K-end
        arr = arr[::-1] 
    
    elif direction == "right":
        print('right')
        arr[-K:] = arr[-K:][::-1]  # Reverse last K elements
        arr[:-K] = arr[:-K][::-1]  # Reverse first n-K elements
        arr = arr[::-1]  
    
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
K = 3
print(rotate_array(arr, K, 'right'))
