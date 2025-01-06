# Second Smallest and Second Largest element in an array.


def second_smallest_largest(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    return f"second smallest - {my_list[1]} \nsecond largest - {my_list[-2]}"

my_list = [9,2,3,5,4,6,8,7,1]
print(second_smallest_largest(my_list))