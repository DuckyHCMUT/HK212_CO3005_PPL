# normal method
def product(lst):
    res = 1
    for i in lst:
        res *= i if type(i) is int else 1
    return res

# recursive method
def product_recur(lst):
    return lst[0] * product(lst[1:]) if type(lst[0]) is int else product(lst[1:]) if lst else 1

# Driver code
print("Normal method result:", product([1.5, 2, "b", "cd", 3, 4]))
print("Recursive method result:", product_recur([1.5, 2, "b", "cd", 3, 4]))
