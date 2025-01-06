# Rearrange array in increasing-decreasing order.

def rearrange_increasing_decreasing(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    return f"increasing -> {my_list} \ndecreasing -> {my_list[::-1]}"

my_list = [9,2,3,5,4,6,8,7,1]
print(rearrange_increasing_decreasing(my_list))