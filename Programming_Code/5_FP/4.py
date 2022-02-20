# Let lst be a list of integer and n be an integer, 
# use list comprehension approach to write function lessThan(lst,n) 
# that returns the list of all numbers in lst less than n.

# Done
def lessThan(lst, n):
    return [i for i in lst if i < n]

# Test 1
print(lessThan([1,2,3,4,5],4))

# Test 2
print(lessThan([],2))

# Test 3
print(lessThan([5,2,6,4,1],3))

# Test 4
print(lessThan([7,6,3,3,5],3))

# Test 5
print(lessThan([1,2,3,-1,0],6))