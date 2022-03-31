from itertools import accumulate

from functools import reduce

# Input: [1, 3, 4, 5]
# Output: [1, 4, 8, 13]
# Traditional method
def subsum_norm(lst):
    res = []
    ele = 0

    for i in lst:
        ele += i
        res.append(ele)
    return res


# High-order function
def subsum_hod(lst):
    return list(accumulate(lst, lambda x, y: x + y))

# Recursive function
def subsum_recur(lst):
    return subsum_recur(lst[:-1]) + [sum(lst)] if lst else [] 

print("Normal method:", subsum_norm([1, 3, 4, 5]))
print("High-order function:", subsum_hod([1, 3, 4, 5]))
print("Recursive method:", subsum_recur([1, 3, 4, 5]))