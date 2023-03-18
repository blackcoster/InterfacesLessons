def decorator(func):
    def wrapper():
        print('функция - оболочка')
        func()
    return wrapper

@decorator
def basic():
    print('я функция')

# wrapped = decorator(basic)
basic()
# wrapped()