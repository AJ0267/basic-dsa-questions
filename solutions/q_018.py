# Replace each element of the array by its rank in the array. 

def replace_with_rank(arr):
    sorted_arr = sorted(arr)
    rank_dict = {}
    rank = 1
    for num in sorted_arr:
        if num not in rank_dict:
            rank_dict[num] = rank
            rank += 1

    result = []
    for num in arr:
        result.append(rank_dict[num])
    return result

# Example usage
arr = [112,115,607,90,504,34]
print(replace_with_rank(arr))
