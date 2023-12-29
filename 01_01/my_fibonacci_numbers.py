def fib(n):
    """Return the n-th Fibonacci number."""
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

print(fib(0))
print(fib(1))
print(fib(8))

print(help(fib))