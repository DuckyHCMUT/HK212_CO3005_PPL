# Write a Python function gcd to return the greatest common divisor (GCD) of two positive integer parameters

def gcd(x, y):
    # Check for smaller parameter
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

# Test 0
print(gcd(24,36))

# Test 1
print(gcd(24,9))

# Test 2	
print(gcd(54,36))

# Test 3	
print(gcd(1071,462))