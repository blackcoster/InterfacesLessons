
def bread(func):
    def wrapper():
        print('булка')
        func()
        print('булка')
    return wrapper

def vegetables(func):
    def wrapper():
        print('помидор')
        func()
        print('салат')
    return wrapper

@bread
@vegetables
def buter():
    print('мясо')

a = bread(vegetables(buter))

buter()