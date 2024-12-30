# Find all repeating elements in an array.

def repeating_elements(arr):
    freq = {}
    repeating = []

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num, count in freq.items():
        if count > 1:
            repeating.append(num)
    
    return repeating

arr = [4, 5, 6, 4, 7, 5, 8, 9, 6]
print(repeating_elements(arr))