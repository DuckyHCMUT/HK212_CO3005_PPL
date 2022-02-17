def increase(n): return n + 1
def square(n): return n * n

def compose(fun1, fun2, *funs):
    return fun1(fun2(funs))
    # increase(square(n))

f = compose(increase, square)
print(f(3)) 
#increase(square(3)) = 10
