def my_decorator(func):
    '''Decorator function'''
    def wrapper():
        '''Return the string in capital letters and with a dash in between each character'''
        print('Before function')
        result = ''
        for char in func():
            result += char.upper() + '-'
        # print(result[:-1])
        print('After function')
        return result[:-1]
    return wrapper



def pfib():
    '''Print out Fibonacci'''
    return 'Fibonacci'

print(pfib())

pfib = my_decorator(pfib)
print(pfib())

@my_decorator
def p2fib():
    '''Print out Fibonacci'''
    return 'Fibonacci'

print(f'now p2fib is {p2fib.__name__}')
print(p2fib())

print(f'now the decorated p2fib function is {p2fib}')