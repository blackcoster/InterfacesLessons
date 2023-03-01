class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def say_name(self):
        print(self.name)

    def say_age(self):
        print(self.age)

    def say(self,words):
        print(words)

class Student(Person):
    def __init__(self,name,surname,age,classnum):
        super().__init__(name,surname,age)
        self.classnum = classnum

    def learn(self):
        print(f'я учусь в {self.classnum} классе')

polina = Person('polina','krupenina',22)
polina.say_age()
polina.say('что-то')
student = Student('polina','krupenina',22,11)
student.learn()

