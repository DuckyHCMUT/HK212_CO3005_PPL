def foo(a, b): pass
x = foo
print(x(3, 4)) # Nothing

def foo_(f, x):
    return f(x)
print(foo_(lambda a: a ** 2, 4))

def f(x):
    def g(y):
        return x*y
    return g

m = f(3)
print(m(4))