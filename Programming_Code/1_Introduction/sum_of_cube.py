# Write a Python function sum_of_cube(n) that takes a positive integer n and returns the sum of the cube of all the positive integers smaller than n

def sum_of_cube(n):
    sum = 0
    for i in range(0, n, 1):
        sum += i*i*i
    return sum

# Test 0 
print(sum_of_cube(8))

# Test 1
print(sum_of_cube(12))

# Test 2
print(sum_of_cube(4))

# Test 3	
print(sum_of_cube(1))