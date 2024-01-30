from time import perf_counter
from functools import wraps

def timer(func):
    '''Print the runtime of the decorated function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f'{func.__name__}({args})  = {result} ->ran in {duration:.8f}s')
        return result
    return wrapper

@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(20)
