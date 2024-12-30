# Adding Element in an array.

def add_elements_in_array(arr, element, position=None):

    if position == None:
        arr.append(element)
    elif position == 0:
        arr.insert(0, element)
    elif 0 < position < len(arr):
        arr.insert(position-1, element)
    else:
        arr.append(element)

    return arr


arr = [1,2,3,5,6,7,8]

# print(add_elements_in_array(arr, 9))
# print(add_elements_in_array(arr, 0, 0))
# print(add_elements_in_array(arr, 4, 4))
# print(add_elements_in_array(arr, 9, 8))