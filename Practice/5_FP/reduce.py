from functools import reduce

# l = reduce(lambda acc, ele: acc + ele, [1,2,3,4])
# print(l)

# l = ['a', 'b', 'c']
# left = reduce(lambda acc, ele: acc + ele, l, 'o')
# print(left)

# right = reduce(lambda acc, ele: ele + acc, l[::-1], 'o')
# print(right)

def lstSquare (n):
    if n == 1:
        return [1]
    else:
        return lstSquare(n-1) + [n*n]

print(lstSquare(5))
