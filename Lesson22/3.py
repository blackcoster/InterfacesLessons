
def decorator(func):
    def wrapper():
        print('начало функции')
        func()
        print('конец функции')
    return wrapper

@decorator
def func():
    print('привет мир')

func()