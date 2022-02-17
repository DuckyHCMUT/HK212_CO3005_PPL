def lessThan(lst, n):
    if not lst:
        return []
    if lst[0] < n:
        return [lst[0]] + lessThan(lst[1:], n)
    else:
        return lessThan(lst[1:], n)

# print(lessThan([1, 2, 3, 4, 5], 4))
print(lessThan([5, 2, 6, 4, 1],3))