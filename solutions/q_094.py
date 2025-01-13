# Write a program to sort characters in a string. 

def sort_characters(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string


print(sort_characters('Hi,1234#@aniket!'))


#using bubble sort
def sort_characters1(string):
    char_list = list(string) 
    n = len(char_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

    sorted_string = ''.join(char_list)
    return sorted_string

print(sort_characters1('Hi,1234#@aniket!'))