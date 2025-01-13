# Program to find sum of GP Series. 

def sum_of_gp(a, r, n):
    if r == 1:
        return a * n  # exceptional case when r = 1
    return a * (1 - r**n) / (1 - r)

print(sum_of_gp(5,2,10))