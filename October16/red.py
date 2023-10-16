
def red(func):
    def wrapper(*args, **kwargs):
        print('\033[31m')
        func(*args, **kwargs)
        print('\033[0m')     
    return wrapper
