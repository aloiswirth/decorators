from functools import wraps

def bold(func):
    '''This is the function decorator'''
    @wraps(func)
    def wrapper():
        '''This is the wrapper function'''
        return f'<b>{func()}</b>'
    return wrapper


def italics(func):
    '''This is the function decorator'''
    @wraps(func)
    def wrapper():
        '''This is the wrapper function'''
        return f'<i>{func()}</i>'
    return wrapper


@bold 
@italics
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'

print(printfib())