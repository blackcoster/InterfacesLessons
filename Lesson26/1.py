class Animal():


    def __init__(self,n):
        self.name = n

    def speak(self):
        print('я говорю')


baran = Animal('бараш')
print(baran.name)