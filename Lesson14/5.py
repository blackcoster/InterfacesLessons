class Animal:
    def __init__(self,type,name = 'безымянный'):
        self.type = type
        self.name = name

    def __sayName(self):
        print(self.name)


cat=Animal('кот')
dog = Animal('собака','Шарик')
cat._Animal__sayName()
dog._Animal__sayName()