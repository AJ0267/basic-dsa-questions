# Sorting elements of an array by frequency. 

# count freq
def count_freq(arr):
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    return freq_map

# highest freq
def highest_freq(freq_map):
    max_freq = -1
    num_to_add = None
    for num, freq in freq_map.items():
        if freq > max_freq:
            max_freq = freq
            num_to_add = num
    return num_to_add, max_freq

def sort_by_frequency(arr):
    freq_map = count_freq(arr)
    sorted_arr = []
    while freq_map:
        num_to_add, max_freq = highest_freq(freq_map)
        for _ in range(max_freq):
            sorted_arr.append(num_to_add)
        del freq_map[num_to_add]
    return sorted_arr

arr = [4, 3, 2, 3, 1, 4, 2, 4]
print(sort_by_frequency(arr))
