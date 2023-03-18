a = 'hello'
iterator = iter(a)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

tuple1 = ('яблоко', 'банан', 'вишня')
myIter = iter(tuple1)
print(next(myIter))
for i in tuple1:
    print(i)