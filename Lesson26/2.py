class Transport:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def beep(self):
        print('beep')

class Car(Transport):
    def __init__(self,speed,color,owner):
        super().__init__(speed,color)
        self.owner = owner

    def say_owner(self):
        print(self.owner)

class Bus(Transport):
    def __init__(self,speed,color,seats):
        super().__init__(speed,color)
        self.seats = seats
    def say_seats(self):
        print(self.seats)

car1 = Car(120,'green','polina')
transport1 = Transport(120,'green')
car1.say_owner()
bus1 = Bus(60,'yellow',40)
bus1.beep()