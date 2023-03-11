a = [1,2,3,4,5,6,7,8,9,10]

a = []
for i in range(1,11):
    a.append(i)

a = [i for i in range(1,11)]
b = [i**2 for i in range(1,11)]
c = [str(i) for i in range(1,11)]
# d = [int(i) for i in input().split()]

e = [i for i in range(1,101) if i%2==0]

d = [i*j for i in range(1,10) for j in [1,2,3] ]
d = [i*j for i in range(1,10) for j in [1,2,3] if (i*j)%2==1]
print(d)
#НЕ КОРТЕЖ a = (i for i in range(1,11))
a = [i for i in range(1,11)]
a = tuple(a)
e = [i if i%2!=0 else i//2 for i in range(1,101)]
print(e)