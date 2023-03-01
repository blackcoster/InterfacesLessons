class MyClass:
    def __init__(self,name):
        self._name = name

    @property # getter получатель переменной
    def name(self):
        print(self._name)

    @name.setter # сеттер редактор переменной
    def name(self,name):
        self._name = name

a = MyClass('polina')
a.name
# a.name('ne polina')
a.name = 'ne polina'
a.name
# a._name = 'ne polina' ТАК НЕ ДЕЛАЕМ
