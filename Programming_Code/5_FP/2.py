# Let lst be a list of integer and n be any value, 
# use recursive approach to write function dist(lst,n) 
# that returns the list of pairs of an element of lst and n.

# Done
def dist(lst, n):
    return [(lst[0], n)] + dist(lst[1:], n) if lst else []

# Test 1
print(dist([1, 2, 3], 4))

# Test 2
print(dist([],4))

# Test 3
print(dist([1,2,3],'a'))

# Test 4
print(dist([3,4,1,5],6))

# Test 5
print(dist([1],'a'))