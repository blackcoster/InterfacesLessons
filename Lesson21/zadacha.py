a = list( map(int,input().split()))

# if a[0]>=a[1]>=a[2]>=a[3]:
#     print('yes')
# elif a[0]<=a[1]<=a[2]<=a[3]:
#     print('yes')
# else:
#     print('no')

if a == sorted(a) or a==sorted(a,reverse=True):
    print('yes')
else: print('no')
