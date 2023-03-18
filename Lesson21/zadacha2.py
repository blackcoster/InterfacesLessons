from math import ceil
n,m,k = list( map(int,input().split()))

vsego_min = ceil(n*k / m)
print(vsego_min)