numbers = [1,2,3,4,5]
result = (x*x for x in numbers)
# for num in result:
#     print(num)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
# print(next(result))
print()
for num in result:
    print(num)

