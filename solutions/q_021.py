# Finding equilibrium index of an array. 

def find_equilibrium(arr):
    total_sum = 0
    left_sum = 0
    equilibrium_indices = []

    # sum
    for num in arr:
        total_sum += num  

    for i in range(len(arr)):
        total_sum -= arr[i]  # Right sum  = total - current ele
        if left_sum == total_sum:  
            equilibrium_indices.append(i)
        left_sum += arr[i] 

    return equilibrium_indices

arr = [-7, 1, 5, 2, -4, 3, 0]
print(find_equilibrium(arr))
