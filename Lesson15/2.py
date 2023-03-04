
class Test(list):
    def append(self,object):
        for i in range(len(self)):
            self[i] **=object


# a=[] == a = list() append(4)
a = Test([1,2,3])
a.append(2)
print(a)
b=Test([5])
b.append(2)
print(b)