from functools import reduce

def flatten(lst):
    if not lst:
        return []
    return reduce(lambda a, b: a + b, lst)

print(flatten([[1,2,3],[4,5],[6,7]]))
print(flatten([]))