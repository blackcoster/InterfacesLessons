dic1 = {'1':'1',
        '2':'4'}
dict1 = {i:i for i in range(1,6)}
dict1 = {i:i**2 for i in range(1,6)}
dict1 = {x:y for x in [1,2,3] for y in [1,2,3]}
dict1 = {x:y for x in 'ABC' for y in "XYZ"}
dict1 = {x:'Z' for x in 'ABC' }
dict1 = {}.fromkeys('ABC','Z')
dict1 = {x:y for x,y in [('A','X'),('B','Y'),('C','Z')]}
dict1 = {x:[i for i in range (1,5)] for x in [1,2,3]}
dict1 = {x:{y:x for y in 'XYZ'} for x in [1,2,3]}
print(dict1)
