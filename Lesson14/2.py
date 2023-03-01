class Human:
    def __init__(self,name,age,classnum = 0,pet = 'нету'):
        self.name = name
        self.age = age
        self.classnum = classnum
        self.pet = pet

polina = Human('polina',22)
bogdan = Human('Bogdan',13,8)
tanya = Human('Tanya',16,10,'cat')
tanya2 = Human('Tanya',18,11)

petr = Human(name = 'Petr',age = 32,pet='dog')