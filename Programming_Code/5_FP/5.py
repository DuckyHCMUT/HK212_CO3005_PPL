# Let lst be a list of a list of element, 
# use list comprehension approach to write function flatten(lst) 
# that returns the list of all elements

# Done
def flatten(lst):
    return [i for sublist in lst for i in sublist]

# Test 1
print(flatten([[1,2,3],[4,5],[6,7]]))

# Test 2
print(flatten([[]]))

# Test 3
print(flatten([]))

# Test 4
print(flatten([[1,2,3]]))

# Test 5
print(flatten([[1],[2],[3],[4],[5,6,7]]))