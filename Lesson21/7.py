a = 'ассоциация'
my_dict = {i:a.count(i) for i in a}
print(my_dict)

dz = (i*2 for i in 'polina')
print(list(dz))