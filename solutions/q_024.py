# Search an element in an array. 


def search_element(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return f"element ({target}) found at index {i}"
    return -1


arr = [10, 20, 30, 40, 50]
target = 30

print(search_element(arr, target))