def power(y):
    def inner(x):
        return x ** y
    return inner

square = power(2)
print(square(5))