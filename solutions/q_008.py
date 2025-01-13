# Rotate array by K elements - Block Swap Algorithm.

def rotate_by_k(arr, K):
    n = len(arr) 
    K = K % n  # when K > n

    # Reverse 0-K elements
    arr[:K] = arr[:K][::-1]
    
    # Reverse K-end
    arr[K:] = arr[K:][::-1]
    
    # Reverse whole array
    arr = arr[::-1]
    return arr 

arr = [1, 2, 3, 4, 5, 6, 7]
K = 3
print(rotate_by_k(arr, K))

