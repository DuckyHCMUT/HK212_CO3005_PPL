# Scala has function compose to compose two functions but Python does not have this function. 
# Write function compose that can takes at least two functions as its parameters and returns the composition of these parameter functions. 
# For example compose(f,g,h)(x) is defined as f(g(h(x))).

# Done
def increase(n): return n + 1
def square(n): return n * n
def double(n): return n * 2
def decrease(n): return n - 1

from functools import reduce

def compose(f1, f2, *fun):
    def composeInner(fun1, fun2):
        return lambda x: fun1(fun2(x))
    return reduce(composeInner, (f1, f2, ) + fun, lambda x:x)

# Driver code
# Test-case 1
f = compose(increase, square)
print(f(3)) 

# Test-case 2
f = compose(increase, square, double)
print(f(3))

# Test-case 3
f = compose(increase, square, double, decrease)
print(f(3))

# Test-case 4a
try:
    f = compose(increase)
except TypeError:
    print("compose() missing 1 required positional argument")

# Test-case 5
try:
    f = compose()
except TypeError:
    print("compose() missing 1 required positional argument")
