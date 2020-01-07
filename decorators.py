#DECORATORS
#HOC
from time import time
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('******')
        func(*args, **kwargs)
        print('******')
    return wrap_func
@my_decorator
def hello():
    print('Yyyeeahhh!!!', 'Bitch', 'Hello', 23)
@my_decorator
def bye():
    print('BYE', 34, 12, True)
hello()
bye()


def perfomance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}ms.')
        return result
    return wrapper
@perfomance
def long_time():
    for i in range(10000000):
        i * 5
long_time()