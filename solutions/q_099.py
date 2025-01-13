# Write a program to find a substring within a string. If found display its starting position. 

def find_substring(main_string, sub_string):
    main_length = len(main_string)
    sub_length = len(sub_string)

    for i in range(main_length - sub_length + 1):
        if main_string[i:i + sub_length] == sub_string:
            return f"Substring found at position {i}"
    return 'substring not found'

main_string = "Hello my name is aniket."
sub_string = "aniket"
print(find_substring(main_string, sub_string))
