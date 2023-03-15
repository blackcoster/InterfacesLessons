f = open('test.txt')
lines = (t.strip() for t in f)
comments = (t for t in lines if t[0]=='#')
for c in comments:
    print(c)
#
# comments_list = list(comments)
# print(comments_list)