# Sum of numbers in the given range.

def sum_of_range(start, end):
    total = 0 
    for number in range(start, end+1):
        total += number
    return total

def sum_of_range_formula(start,end):
    n = end - start+1
    total = n*(start+end) // 2
    return total


print(sum_of_range(1,10))
print(sum_of_range_formula(5,13))