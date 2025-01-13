# Rotate array by K elements - Block Swap Algorithm.

def rotate_by_k(arr, K):
    n = len(arr) 
    K = K % n  # when K > n
    arr[:K] = arr[:K][::-1] # Reverse 0-K elements
    arr[K:] = arr[K:][::-1] # Reverse K-end
    arr = arr[::-1] # Reverse whole array
    return arr 

arr = [1, 2, 3, 4, 5, 6, 7]
K = 3
print(rotate_by_k(arr, K))

