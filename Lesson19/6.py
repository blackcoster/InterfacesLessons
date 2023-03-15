# 1 1 2 3 5 8 13 21 34 55
def fib(n):
    fib0 = 1
    yield fib0
    fib1 = 1
    yield fib1
    for i in range(n-2):
        fib0,fib1 = fib1,fib0+fib1
        yield fib1

for num in fib(100):
    pass

print(num)

# 1 1
# 1 2
# 2 3
# 3 5
# 5 8
# 8 13
# 13 21
