# Write a Python function check(lst,n) to test whether all numbers of the list lst is greater than the number n

def check(lst, n):
    for i in lst:
        if (i <= n):
            return False
    return True

# Test 0
print(check([21,12,5,8],3))

# Test 1
print(check([21,12,5,8],7))

# Test 2	
print(check([21,12,5,8],22))

# Test 3
print(check([21,12,1000,100,90],11))

# Test 4
print(check([21,12,1000,100,90],12))

