#Find all non-repeating elements in an array.

def non_repeating_elements(arr):
    freq = {}
    non_repeating = []

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num, count in freq.items():
        if count == 1:
            non_repeating.append(num)
    
    return non_repeating

arr = [4, 5, 6, 4, 7, 5, 8, 9, 6]
print(non_repeating_elements(arr))
