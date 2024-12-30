# Average of all elements in an array.

def find_average(arr):
    n = len(arr)
    total_sum = sum(arr)

    if n == 0:
        return None
    return total_sum / n

arr = [10,20,40,50,30]
print(find_average(arr))