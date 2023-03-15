def func(num):
    while num > 0:
        yield num
        num-=1

# for num in func(5):
#     print(num)
result = func(5)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())

for num in func(5):
    print(num)
a = sum(func(5))
print(a)