# Write a Python function product(lst) to return the product of the list lst of integers

def product(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod

# Test 0
print(product([3,4,7,11]))

# Test 1
print(product([3]))

# Test 2
print(product([3,4]))

# Test 3
print(product([3,4,7]))


