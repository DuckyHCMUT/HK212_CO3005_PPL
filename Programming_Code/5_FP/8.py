# Use high-order function approach to write function lstSquare(n:Int) 
# to return a list of i square for i from 1 to n?

# Done
def lstSquare(n):
    return list(map(lambda x: x * x, range(1, n + 1)))

# Test 1
print(lstSquare(3))

# Test 2
print(lstSquare(1))

# Test 3
print(lstSquare(5))

# Test 4
print(lstSquare(4))