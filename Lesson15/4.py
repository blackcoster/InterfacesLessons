class Point:

    count =0
    def __init__(self,x,y):
        self.x = x
        self.y = y

        Point.count+=1

    def __str__(self):
        return f'Точка с координатами {self.x},{self.y}  '

    def __add__(self,other):
        if isinstance(other,Point)==1:
            return Point(self.x+other.x,self.y+other.y)


    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __neg__(self):
        return Point(-self.x, -self.y)
    def __eq__(self, other):
        return Point(self.x == other.x, self.y == other.y)

    @staticmethod
    def sum(*points):
        res = points[0]
        for p in points[1:]:
            res+=p
        return res

    @classmethod
    def from_string(cls,str):
        values = [int(x) for x in str.split(',')]
        # s = str.split(',')
        # for i in s:
        #     i=int(i)
        return cls(*values)

a = Point(2,4)
b = Point(2,4)
print(a+b)
print(Point.count)
c= Point.sum(a,b)
print(c)
c = Point.from_string('1,3')
print(c)