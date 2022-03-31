def f(x = None):
    def g(x):
        return x*x
    return x*g(x)

def h(x):
    return lambda y: x + y  # Return a closure.

print(f(6))
print(h(10))