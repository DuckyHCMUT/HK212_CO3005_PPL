from itertools import accumulate

# Helper function
def makelist(n):
    return list(map(int, str(n)))

def getSubSum(n):
    return list(accumulate(makelist(n), lambda a, b: a + b))

# Driver code
print(getSubSum(142))