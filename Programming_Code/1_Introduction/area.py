# Write a Python function, whose name is area, which accepts the radius of a circle as an input parameter and return the area

import math as m

def area(r):
    return r*r*m.pi

# Test 0
res = area(1.1)
expect = 3.8013271108436504
delta = 0.000000001
print((res > expect - delta) and (res < expect + delta))

# Test 1
res = area(2.6)
expect = 21.237166338267002
delta = 0.000000001
print((res > expect - delta) and (res < expect + delta))

# Test 2
res = area(12.6)
expect = 498.75924968391547
delta = 0.000000001
print((res > expect - delta) and (res < expect + delta))

# Test 3	
res = area(102.45)
expect = 32974.164346060104
delta = 0.000000001
print((res > expect - delta) and (res < expect + delta))
