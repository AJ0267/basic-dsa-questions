# Find all symmetric pairs in array. 

def find_symmetric_pairs(arr):
    pairs = {}
    symmetric_pairs = []

    for a, b in arr:
        if (b, a) in pairs:
            symmetric_pairs.append((a, b))
        else:
            pairs[(a, b)] = True

    return symmetric_pairs


print(find_symmetric_pairs([(1, 2), (3, 5), (2, 1), (5, 3), (4, 7)]))