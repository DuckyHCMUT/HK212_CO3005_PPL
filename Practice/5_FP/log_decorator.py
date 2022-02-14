def log_decorator(func):
    def inner(*arg):
        print(func.__name__+" is running")
        return func(*arg)
    return inner

@log_decorator
def foo(x, y):
    return x*y
    
print(foo(3,4))