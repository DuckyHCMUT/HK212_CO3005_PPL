# Use list comprehension approach to write a function lstSquare(n:Int) 
# that returns a list of the squares of the numbers from 1 to n?

# Done
def lstSquare(n):
    return [i*i for i in [i for i in range(1, n + 1)]]

# Test 1
print(lstSquare(3))

# Test 2
print(lstSquare(1))

# Test 3
print(lstSquare(5))

# Test 4
print(lstSquare(4))