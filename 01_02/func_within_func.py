def fib_three(a,b,c):
    '''Accepts as input 3 Fibonacci numbers'''
    def get_three():
        '''Returns the three Fibonacci numbers'''
        return a,b,c
    return get_three

print(fib_three(1, 1, 2))

f = fib_three(1, 1, 2)
print(f())