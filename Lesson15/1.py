class Parent:
    def say_hello():
        print('я метод родительского класса')

class Child(Parent):
    def say_hello():
        print('я метод детского класса')
a = Child
a.say_hello()

