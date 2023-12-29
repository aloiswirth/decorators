'''
Fixed arguments
'''
# def print_fib(a, b, c):
#     print(a, b, c)

# print_fib(1, 1, 2)

# # print_fib(1, 1, 2, 3)
# # this returns an error as the function is expecting 3 arguments but 4 are passed

# '''
# Using *args
# '''
# def print_fib(a, *args):
#     print(a)
#     print(args)

# print_fib(1, 1, 2, 3)

# print_fib(1)

# # print_fib()
# # This returns an error as the function is expecting at least 1 argument but none are passed

# '''
# Using **kwargs
# '''
# def print_fib(a, **kwargs):
#     print(a)
#     print(kwargs)

# print_fib(1, se=1, th=2, fo=3, fi=5)

# print_fib(1)

# # print_fib()
# # This returns an error as the function is expecting at least 1 argument but none are passed

'''
Using *args and **kwargs
'''


# print_fib(1, 1, 2, 3)

# print_fib(fi=1, se=1, th=2, fo=3)

# print_fib(1, 1, 2, fo=3, fi=5)

# print_fib()
# This returns an empty tuple and dictionary as no arguments are passed
def display_args(func):
    def wrapper(*args, **kwargs):
        print(args)
        print(*args)
        print("leaving the wrapper")
        result = func(*args, **kwargs)
        return result
    return wrapper


@display_args
def print_fib(*args, **kwargs):
    print(args)
    print(kwargs)


print_fib(1, 1, 2, le=3, la=5)
