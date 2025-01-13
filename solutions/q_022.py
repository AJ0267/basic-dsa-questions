#Finding circular rotation of an array by K positions.

def rotate_array(arr, K):
    K = K % len(arr)   #when K > len(arr)
    rotated_array = arr[-K:] + arr[:-K]
    return rotated_array


arr = [1, 2, 3, 4, 5]
K = 2
print(rotate_array(arr, K))