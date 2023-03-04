# a=3
# b=5
# a+b
# __str__
# x<y x.__lt__(y) x==y __eq__
# print(a) -> a.__str__
# a.__add__(b)

class Test(int):
    def __init__(self,num):
        super().__init__()
        self.num = num
    def __add__(self, num2):
        return self.num * num2

a = Test(3)
b = Test(5)
print(a+b)