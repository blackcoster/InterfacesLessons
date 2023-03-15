def func():
    while True:
        n = yield
        print(n**2)

r = func()
r.send(None)
r.send(1)
r.send(3)
r.send(7)
r.close()
# r.send(3)
