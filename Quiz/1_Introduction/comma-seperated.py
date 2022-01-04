# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# For example:
# Input: 13,2,4,5
# Output: 
# [13,2,4,5]
# (13,2,4,5)

inpString = input()
inpList, inpTuple = list(inpString.split(',')), tuple(inpString.split(','))
print(inpList)
print(inpTuple)

# Test 0: 
# 13,2,4,5

# Test 1: 	
# 12

# Test 2
# 1,2

# Test 3
# 1,  3,4,15,22,16,7


