# Count frequency of each element in an array.

def count_frequency(arr):
    if len(arr) == 0:
        return None
     
    freq_dict = {}

    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    return freq_dict


arr = [42, 30, 1, 3, 4, 4, 30, 42 , 42, 3, 1, 6]
print(count_frequency(arr))