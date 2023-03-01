class Person:
    _age = 15

    def __say(self):
        print('hello')


p = Person()
print(p._age)
# p.__say()
p._Person__say()