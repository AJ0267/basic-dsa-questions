# Find sum of AP Series.

def sum_of_ap(a, d, n):
    #formula of sum of AP = n/2 * (2a + (n-1) * d)
    return n / 2 * (2 * a + (n - 1) * d)


print(sum_of_ap(5,3,10))