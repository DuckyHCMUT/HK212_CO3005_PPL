# Normal method
def ham(lst, n):
    res = []
    for i in lst:
        res.append((i, n))
    return res

# Recursive method
def ham_recur(lst, n):
    return [(lst[0], n)] + ham_recur(lst[1:], n) if lst else []

# High-order function
def ham_highorder(lst, n):
    return list(map(lambda a: (a, n), lst))

# List comprehension method
def ham_listcomp(lst, n):
    return [(a, n) for a in lst]

# Driver code
print("Normal method result:", ham([1, 2, 3], 4))
print("Recursive method result:", ham_recur([1, 2, 3], 4))
print("High-order function method result:", ham_highorder([1, 2, 3], 4))
print("List comprehension method result:", ham_listcomp([1, 2, 3], 4))