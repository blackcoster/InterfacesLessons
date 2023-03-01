class Cars:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color

    def beep(self):
        print('beeeeeeeeep')

class Human:
    def __init__(self,name):
        self.name = name
    def walk(self):
        print('я хожу')

class Transformer(Human,Cars):
    pass


tr1 = Transformer('Bumblebee')
tr1.beep()
tr1.walk()