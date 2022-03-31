def makelist(n):
    return [int(x) for x in str(n)]

def makelist_recur(n):
    if n < 10:
        return [n]
    return makelist_recur(n // 10) + [n%10]

def makelist_hod(n):
    return list(map(int, str(n)))

# Driver code
print("Normal: ", makelist(142))

print("Recursive:", makelist_recur(142))
print("Recursive:", makelist_recur(140))

print("HOD:", makelist_recur(142))
print("HOD:", makelist_recur(140))
