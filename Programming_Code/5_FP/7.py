def lstSquare(n):
    lst = [i for i in range(1, n + 1)]
    return [i*i for i in lst]

print(lstSquare(3))