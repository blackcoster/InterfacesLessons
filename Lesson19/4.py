def func():
    yield 37
    # yield 38
    return 42

result = func()
print(result)
print(next(result))
print(next(result))