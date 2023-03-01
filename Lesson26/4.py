class Transport:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def beep(self):
        print('beeeeeeeeep транспортный')

class Car(Transport):
    def __init__(self,speed,color,owner):
        super().__init__(speed,color)
        self.owner = owner

    def say_owner(self):
        print(self.owner)

    def beep(self):
        print('бип машинный')
        
class SportCar(Car,Transport):
    pass

tr1 = Transport(120,'red')
car1 = Car(120,'black','polina')

tr1.beep()
car1.beep()